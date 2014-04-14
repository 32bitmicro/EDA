# -*- coding: utf-8 -*-
#
# Copyright (c) 2014, Paweł Wodnicki
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the 32bitmicro nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.

#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL Paweł Wodnicki BE LIABLE FOR ANY
#DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from edautils import *
from eda import *

from ctypes import *



# ctypes based point structure
class POINT(Structure):
    _fields_ = ("x", c_int), ("y", c_int)


class CRoute:
    " Route class "
    def __init__(self, sch=None,brd=None):
        self.name=""
        self.sch=sch
        self.brd=brd
        self.routed_nets = 0
        self.blockages=[]
        self.blockage_cost = 1000                     # scaling for the blockages
        self.route_cost = 1
        self.grid = 1000                              # 10 mil grid
        #self.grid = 100                               # 1 mil grid
        self.blockage_map = None
        self.blockage_map_nx = 0
        self.blockage_map_ny =0
        
        
    def createBlockageMap(self, bs):
        rect = bs.outline.bbox
        # scan all Z shapes solutions along line connecting both points
        self.blockage_map_nx = nx = int(rect.ur._x / self.grid) + 1
        self.blockage_map_ny = ny = int(rect.ur._y / self.grid) + 1
    
        print "blockage map  on a grid " + str(self.grid)
        print "nx   " + str(self.blockage_map_nx)
        print "ny   " + str(self.blockage_map_ny)
        
        self.blockage_map = Matrix(nx,ny,0)
        
        self.addBlockagesToBlockageMap()
        # very very inneficient do not use!
#        for ry in range(ny):
#            for rx in range(nx):
#                pX = rx * self.grid
#                pY = ry * self.grid
#                for brect in self.blockages:
#                    if brect.isInside(pX,pY):
#                        self.blockage_map[rx][ry] = 10000
    
    # this is more efficient        
    def addBlockagesToBlockageMap(self):
        for brect in self.blockages:
            X1 = brect.ll._x
            Y1 = brect.ll._y
            X2 = brect.ur._x
            Y2 = brect.ur._y
            print "add blockages to map "
            nx = int (abs(X2-X1) / self.grid) + 1
            ny = int (abs(Y2-Y1) / self.grid) + 1
                
            sx = int (X1 / self.grid)
            sy = int (Y1 / self.grid)
            
            print " sx " + str(sx) + " nx "  + str(nx) 
            print " sy " + str(sy) + " ny "  + str(ny) 
            
            for ry in range(ny):
                #print "ry " + str(ry)
                for rx in range(nx):
                    #print "rx " + str(rx)
                    pX = int(sx + rx)
                    pY = int(sy + ry)
                    #print "pX   " + str(pX)
                    #print "pY   " + str(pY)
                    self.blockage_map[pX][pY] = 10000 # weight
                    #print str(self.blockage_map[pX][pY])
                    
                    
        
    def addRouteToBlockageMap(self,route):
        pass
            
        
    def addLineToBlockageMap(self,line):
        # add line to blockage map
        first = True
        prev  = Point()
        for pt in line.points:
            print "pt  " + str(pt)
            if first:
                first = False
                prev = pt
            else:
                X1 = prev._x
                Y1 = prev._y
                X2 = pt._x
                Y2 = pt._y
                
                if X1 > X2:
                    tmp = X1
                    X1 = X2
                    X2 =tmp
                    
                if Y1 > Y2:
                    tmp = Y1
                    Y1 = Y2
                    Y2 =tmp
                
                print "add line to map " +str(prev) + " - "  + str(pt)
                nx = int (abs(X2-X1) / self.grid) + 1
                ny = int (abs(Y2-Y1) / self.grid) + 1
                
                sx = int (X1 / self.grid)
                sy = int (Y1 / self.grid)
                
                print " sx " + str(sx) + " nx "  + str(nx) 
                print " sy " + str(sy) + " ny "  + str(ny) 
                
                for ry in range(ny):
                    #print "ry " + str(ry)
                    for rx in range(nx):
                        #print "rx " + str(rx)
                        pX = int(sx + rx)
                        pY = int(sy + ry)
                        self.blockage_map[pX][pY] = 10000 # weight
                        #print str(self.blockage_map[pX][pY])
                
                prev = pt
                
    
    def genBlockagesFromPads(self,dev,pad):
        lnum = 6
        lname = "blkcomponent"    
        if dev.bottom:
            lnum = 5
            lname = "blksolder"
        
        X1=int(pad.bbox.ll._x)
        Y1=int(pad.bbox.ll._y)
        X2=int(pad.bbox.ur._x)
        Y2=int(pad.bbox.ur._y)
        
        l = self.brd.getLayer(lname)
        if l:
            x1 = dev.position._x + X1
            y1 = dev.position._y + Y1
            x2 = dev.position._x + X2
            y2 = dev.position._y + Y2
            blk = Rectangle(x1,y1,x2,y2,lnum)
            l.blockages.append(blk)
            self.blockages.append(blk)
        
    def genBlockagesFromPins(self,dev,pin):       
        l = self.brd.getLayer("blksolder")
        if l:
            x1 = dev.position._x + pin.bbox.ll._x
            y1 = dev.position._y + pin.bbox.ll._y
            x2 = dev.position._x + pin.bbox.ur._x
            y2 = dev.position._y + pin.bbox.ur._y
            blk = Rectangle(x1,y1,x2,y2,5)
            l.blockages.append(blk)
            self.blockages.append(blk)
            
        l = self.brd.getLayer("blkcomponent")
        if l:
            x1 = dev.position._x + pin.bbox.ll._x
            y1 = dev.position._y + pin.bbox.ll._y
            x2 = dev.position._x + pin.bbox.ur._x
            y2 = dev.position._y + pin.bbox.ur._y
            blk = Rectangle(x1,y1,x2,y2,6)
            l.blockages.append(blk)
            self.blockages.append(blk)
    
    def genBlockagesFromDevice(self,dev):
        # absolute coordinates
        for pin in dev.pins.values():
            if dev.package.smt:
                self.genBlockagesFromPads(dev,pin)
            else:
                self.genBlockagesFromPins(dev,pin)
                
    def genBlockages(self, bs):
        # Walk all devices and for generate blockage for each pin and pad
        # pin all layers
        # pad only one layer top or bottom
        for dev in bs.devices.values():
            self.genBlockagesFromDevice(dev)
    
    def routeNetHorV(self,net):
        """ Route single net
                Horizontal or vertical
        """
        # only 2 pin nets are considered
        if len(net.nodes) !=2 :
            return
        n1 = net.nodes[0]
        n2 = net.nodes[1]
        X1 = n1.pin.pos._x
        Y1 = n1.pin.pos._y
        X2 = n2.pin.pos._x
        Y2 = n2.pin.pos._y
        
        if (X1 != X2) & (Y1 != Y2):
            return
        # make single connecting line
        ln = Line()
        ln.points=[]
        ln.append(Point(X1,Y1))
        ln.append(Point(X2,Y2))
        # tag net and update statistics
        net.tag = net.tag + 1
        self.routed_nets = self.routed_nets + 1
    
    # calculate routing cost of the line between points s and e
    # return value is line cost and blockage cost separate
    def lineCost(self,sX,sY,eX,eY):
        #print "line cost " + str(sX) + ' ' + str(sY) + ' ' + str(eX) + ' ' + str(eY)
        # make normalized rectangle
        lr = Rectangle(sX,sY,eX,eY)
        #print "line cost " + str(lr)
        hor = False
        vert = False
        lcost = 0
        bcost = 0
        if sX == eX:
            vert= True
            lcost = abs(eY - sY) * self.route_cost
            
        if sY == eY:
            hor= True
            lcost = abs(eX - sX) * self.route_cost
        
        if not (hor | vert):    # neither horizontal or vertical line
            return 1/0
        
#        #print "cost line " + str(cost)    
#        # scan blockages and determine cost
#        for brect in self.blockages:
#            # x interference conditions
#            # line rect ll._x < blk rect ur._x
#            # and 
#            # line rect ur._x > blk rect ll._x
#            
#            # y interference conditions
#            # line rect ll._y < blk rect ur._y
#            # and 
#            # line rect ur._y > blk rect ll._y
#            #print "scan blk "   + str(brect)
#            # check for necessary condition, for horizontal or vertical lines this is enough!
#            if (lr.ll._x <= brect.ur._x) & (lr.ur._x >= brect.ll._x) & (lr.ll._y <= brect.ur._y) & (lr.ur._y >= brect.ll._y):
#            #if (lr.ll._x <= brect.ur._x) & (lr.ur._x >= brect.ll._x):
#            #if (lr.ll._y <= brect.ur._y) & (lr.ur._y >= brect.ll._y):
#                #print "hit blk " + str(brect)
#                if hor:
#                    #print "hor"
#                    lx1 = lr.ll._x
#                    if lx1 < brect.ll._x:
#                        lx1 = brect.ll._x     
#                    lx2 = lr.ur._x
#                    if lx2 > brect.ur._x:
#                        lx2 = brect.ur._x
#                    #print "lx1, lx2 " + str(lx1) + ' ' + str(lx2)
#                    bcost += (lx2-lx1) * self.blockage_cost
#                if vert:
#                    #print "vert"
#                    ly1 = lr.ll._y
#                    if ly1 < brect.ll._y:
#                        ly = brect.ll._y     
#                    ly2 = lr.ur._y
#                    if ly2 > brect.ur._y:
#                        ly = brect.ur._y
#                    #print "ly1, ly2 " + str(ly1) + ' ' + str(ly2)
#                    bcost += (ly2-ly1) * self.blockage_cost
                    
                    
        # scan blockage map
        X1 = sX
        Y1 = sY
        X2 = eX
        Y2 = eY
        lnbcost = 0
        
        if X1 > X2:
            tmp = X1
            X1 = X2
            X2 =tmp
            
        if Y1 > Y2:
            tmp = Y1
            Y1 = Y2
            Y2 =tmp
        
        #print "scan line " +str(Point(X1,Y1)) + " to "  + str(Point(X2,Y2))
        nx = int (abs(X2-X1) / self.grid) + 1
        ny = int (abs(Y2-Y1) / self.grid) + 1
        
        sx = int (X1 / self.grid)
        sy = int (Y1 / self.grid)
        
        #print " sx " + str(sx) + " nx "  + str(nx) 
        #print " sy " + str(sy) + " ny "  + str(ny) 
        
        for ry in range(ny):
            for rx in range(nx):
                x = int(sx + rx)
                y = int(sy + ry)
                #print " x "  +str(x) + " y " + str(y) 
                if (y < self.blockage_map_ny) & (y >= 0):
                    if (x < self.blockage_map_nx) & (x >= 0):
                        co = self.blockage_map[x][y]
                    else:
                        #print "x out of range " + str(x)
                        co = 10000
                else:
                    #print "y out of range " + str(y)
                    co = 10000
                    
                lnbcost += co
                #if co > 0:
                #    print '(' + str(x) +',' + str(y) +')=' + str(co)
        #if lnbcost > 0:
        #    print "lcost " + str(lcost) + " bcost " + str(bcost) + " lnbcost " + str(lnbcost)
        # add to cost
        bcost += lnbcost
        return lcost, bcost

    def routeNetBoxed(self,net):
        """ Route single net boxed using Z shape
                
        """
        # only 2 pin nets are considered
        if len(net.nodes) !=2 :
            return
        
        n1 = net.nodes[0]
        n2 = net.nodes[1]
        X1 = n1.pin.pos._x
        Y1 = n1.pin.pos._y
        X2 = n2.pin.pos._x
        Y2 = n2.pin.pos._y
        best_route = Line()
        best_route.layernum = 1
        best_route.append(Point(X1,Y1))
        best_route.append(Point(X2,Y2))
        
        best_cost = 10000 * 10000 # what is max int?
        
        # scan all Z shapes solutions along line connecting both points
        nx = (X2 - X1) / self.grid
        ny = (Y2 - Y1) / self.grid
        
        dX = (X2 - X1) / nx
        dY = (Y2 - Y1) / ny
        print "net  " + net.name
        print "nx   " + str(nx) + " dX " + str(dX)
        print "ny   " + str(ny) + " dY " + str(dY)
        for ry in range(ny):
            for rx in range(nx):
                pX = X1 + rx * dX
                pY = X1 + ry * dY
                # Left side Up and Down routes
                costLDown = self.lineCost(X1,Y1,pX,Y1) + self.lineCost(pX,Y1,pX,pY)
                costLUp   = self.lineCost(X1,Y1,X1,pY) + self.lineCost(X1,pY,pX,pY)
                # Right side Up and Down routes
                costRDown = self.lineCost(pX,pY,X2,pY) + self.lineCost(X2,pY,X2,Y2)
                costRUp   = self.lineCost(pX,pY,pX,Y2) + self.lineCost(pX,Y2,X2,Y2)
                cost = 0
                route = Line()
                route.layernum = 1
                route.points=[]
                route.append(Point(X1,Y1))
                
                if costLDown < costLUp:
                    cost += costLDown
                    route.append(Point(pX,Y1))
                    print "select LD " + str(pX) + " " + str(Y1)
                else:
                    cost += costLUp
                    route.append(Point(X1,pY))
                    print "select LU " + str(X1) + " " + str(pY)
                    
                if costRDown < costRUp:
                    cost += costRDown
                    route.append(Point(X2,pY))
                    print "select RD " + str(X2) + " " + str(pY)
                else:
                    cost += costRUp
                    route.append(Point(pX,Y2))
                    print "select RU " + str(pX) + " " + str(Y2)
                
                if cost < best_cost:
                    best_cost = cost
                    del best_route
                    best_route = route
        
        net.route.append(best_route)            
        # tag net and update statistics
        net.tag = net.tag + 2
        self.routed_nets = self.routed_nets + 1
    
 
        
    def routeLSegmentWithCost(self,X1,Y1,X2,Y2):
        """ Route L segment between points                
        """
        #print "route L " + str(X1) + ' ' + str(Y1) + ' ' + str(X2) + ' ' + str(Y2)
        # Left side Up and Down routes
        #print "calc cost Down"
        cLine,cBlk = self.lineCost(X1,Y1,X2,Y1)
        costLDown  = cLine + cBlk 
        cLine,cBlk = self.lineCost(X2,Y1,X2,Y2)
        costLDown += cLine + cBlk 
        #print "calc cost Up"
        cLine,cBlk = self.lineCost(X1,Y1,X1,Y2) 
        costLUp    = cLine + cBlk 
        cLine,cBlk = self.lineCost(X1,Y2,X2,Y2)
        costLUp   += cLine + cBlk 
        
        #print "cost Down " + str(costLDown)
        #print "cost Up   " + str(costLUp)
        if costLDown < costLUp:
            #print "selected Down\n"
            return X2,Y1,costLDown
        else:
            #print "selected Up\n"
            return X1,Y2,costLUp
        
    def routeLSegment(self,X1,Y1,X2,Y2):
        """ Route L segment between points                
        """
        rX,rY,rCost = self.routeLSegmentWithCost(X1,Y1,X2,Y2)
        return rX,rY
        
    def routeL2SegmentWithCost(self,X1,Y1,X2,Y2):
        """ Route L2 segment between points                
        """
        print "route L2 " + str(X1) + ' ' + str(Y1) + ' ' + str(X2) + ' ' + str(Y2)
        
        # First route L segment 
        pX,pY = self.routeLSegment(X1,Y1,X2,Y2)
        
        # determine delta around point p, only 45 degree, symetrical
        if ( pX == X1):
            dd = pY - Y1
            if ( X1 + dd ) > X2:
                dd = X2 - X1
        else:
            dd = pX - X1
            if ( Y1 + dd ) > Y2:
                dd = Y2 - Y1
        # symetrical        
        #dd += 2 * dd
        dd = abs(dd)
        
        
            
        best_points = []        
        best_cost = 10000 * 10000 # what is max int?
        
        # scan all Z shapes solutions along line connecting both points
        nx = (dd) / self.grid
        if nx <=0:
            nx = 1
        # limit the number
        if nx > 8:
            nx = 8
        
        ny = (dd) / self.grid
        if ny <=0:
            ny = 1
        # limit the number
        if ny > 8:
            ny = 8
            
        dX = (dd) / nx
        dY = (dd) / ny
        print "dd   " + str(dd)
        print "nx   " + str(nx) + " dX " + str(dX)
        print "ny   " + str(ny) + " dY " + str(dY)
        for ry in range(-ny,ny*2):
            for rx in range(-nx,nx*2):
                ppX = pX + rx * dX
                ppY = pX + ry * dY
                lX,lY,lCost = self.routeLSegmentWithCost(X1,Y1,ppX,ppY)
                rX,rY,rCost = self.routeLSegmentWithCost(ppX,ppY,X2,Y2)
                cost = lCost + rCost
                    
                if cost < best_cost:
                    best_cost = cost
                    best_points = []
                    best_points.append([X1,Y1])
                    best_points.append([lX,lY])
                    best_points.append([ppX,ppY])
                    best_points.append([rX,rY])
                    best_points.append([X2,Y2])
        
        return best_points, best_cost
                    
        
    def routeNet(self,net, bs):
        """ Route single net"""
        #if net.name in ['X1']:
        #    pass
        #else:
        #    return
        #print "routing net:" + net.name
        # brain dead aproach, just connect sequential pins wih L shape
        first = True
        prev = Point()
        mid  = Point()
        curr = Point()
        #ln = Line()
        for node in net.nodes:
            dev = bs.getDev(node.devrefid)
            pin = dev.pinsbyname[node.pinname]
            
            #print str(node.dev)
            #print str(node.dev.package)
            #print "node.pin.pos " + node.pin.name + ' ' + str(node.pin.pos)
            #print "pin.pos      " + pin.name + ' ' + str(pin.pos)
            if first:
                #prev = Point(dev.position._x  + pin.pos._x, dev.position._y + pin.pos._y)
                prev = Point(node.pin.pos._x + node.dev.position._x, node.pin.pos._y + node.dev.position._y)
                first = False
            else:
                #curr = Point(dev.position._x  + pin.pos._x, dev.position._y + pin.pos._y)
                curr = Point(node.pin.pos._x + node.dev.position._x, node.pin.pos._y + node.dev.position._y)
                
                # Starting point
                #rX,rY = self.routeLSegment(prev._x, prev._y,curr._x, curr._y)
                
                route_coordinates, cost = self.routeL2SegmentWithCost(prev._x, prev._y,curr._x, curr._y)
                
                # makes a preference
                #mid = Point(prev._x, curr._y)
                #mid = Point(rX, rY)
#                dx = abs(prev._x - curr._x)
#                dy = abs(prev._x - curr._x)
                ln = Line()
# something strange is going here, the __init__ in Line() does not set points to [] empty list,
# instead it seems to recycle points from previouse instance and points keep accumulating
# is this a Python bug?
                ln.points=[]
                #print "ln.points length start " + str(len(ln.points))
                #ln.append(prev)
                
                for co in route_coordinates:
                    mid = Point(co[0],co[1])
                    ln.append(mid)
                    
                #ln.append(curr)
                ln.layernum = 1        # for now put it on solder
                net.route.append(ln)
                #print "append net" + net.name
                #print "prev     " + str(prev)
                #print "mid      " + str(mid)
                #print "curr     " + str(curr)
                prev = curr
                #print "net.route length " + str(len(net.route))
                #print "ln.points length " + str(len(ln.points))
                
                self.addLineToBlockageMap(ln)
                del ln
            
        # tag net and update statistics
        net.tag = net.tag + 1
        self.routed_nets = self.routed_nets + 1
        
    def routeBoard(self):
        """ Route board """
        
        print "create blockages"
        self.brd.outline.calcBBox()
        self.genBlockages(self.brd)
        #blk = Rectangle(0,0,200000,2000000)
        #self.blockages.append(blk)
        
        print "create blockage map"
        self.createBlockageMap(self.brd)
        
        print "select nets to route"
        # First tag all nets
        for net in self.brd.nets.values():
            net.tag = 0
            #if net.name in ['X1', 'X2']:
            #    net.tag = 0
            #else:
            #    net.tag = -1
        
        print 'route nets'
        # Route Horizontal or Vertical nets
        #for net in self.brd.nets.values():
            #if net.tag == 0:
            #    self.routeNetHorV(net)
        print "nets routed so far " + str(self.routed_nets)
        
        # Route Z shaped nets boxed
        #for net in self.brd.nets.values():
            #if net.tag == 0:
            #    self.routeNetBoxed(net)
        print "nets routed so far " + str(self.routed_nets)
        
        # Finaly just route all remaining nets
        for net in self.brd.nets.values():
            if net.tag == 0:
                self.routeNet(net, self.brd)
        print "nets routed so far " + str(self.routed_nets)
        
    def routeSchematic(self):
        """ Route schematic """
        
        print "create blockages"
        self.sch.outline.calcBBox()
        self.genBlockages(self.sch)
        
        print "create blockage map"
        self.createBlockageMap(self.sch)
        
        print "select nets to route"
        # First tag all nets
        for net in self.sch.nets.values():
            net.tag = 0
        
        print 'route nets'
        # Route Horizontal or Vertical nets
        #for net in self.brd.nets.values():
            #if net.tag == 0:
            #    self.routeNetHorV(net)
        print "nets routed so far " + str(self.routed_nets)
        
        # Route Z shaped nets boxed
        #for net in self.brd.nets.values():
            #if net.tag == 0:
            #    self.routeNetBoxed(net)
        print "nets routed so far " + str(self.routed_nets)
        
        # Finaly just route all remaining nets
        for net in self.sch.nets.values():
            if net.tag == 0:
                self.routeNet(net, self.sch)
        print "nets routed so far " + str(self.routed_nets)
        
