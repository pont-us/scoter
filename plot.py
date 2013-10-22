#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.font_manager import FontProperties
from matplotlib.backends.backend_pdf import FigureCanvasPdf, PdfPages

font_props = FontProperties()
font_props.set_size('x-small')

class WarpLine:
    def __init__(self, bwarp, scale = None,
                 subseries = 0, invert = False, **args):
        self.bwarp = bwarp
        self.args = args
        if scale == None:
            self.scale = (bwarp.series[1].series[subseries].end() /
                          bwarp.series[0].series[subseries].end()
                          )
        else:
            self.scale = scale
        self.subseries = subseries
        self.invert = invert

    def plot(self, axes, xoffset = 0, yoffset = 0):
        bw = self.bwarp        
        xs, ys = self.bwarp.get_rates(scale = self.scale,
                                      invert = self.invert)
        axes.plot(xs, ys,
                  label = self.bwarp.name, **self.args)

    def add_args(self, new_args):
        self.args.update(new_args)

class Line:
    def __init__(self, series, **args):
        self.series = series
        self.args = args

    def plot(self, axes, yoffset = 0, xoffset = 0):
        s = self.series
        axes.plot(s.data[0] + xoffset, s.data[1] + yoffset,
                  label = s.name, **self.args)

    def add_args(self, new_args):
        self.args.update(new_args)

class Axes:
    def __init__(self, lines, invert = False, spread = 0, xspread = 0,
                 xlim = (None, None), ylim = (None, None),
                 xlabel = None, ylabel = None):
        if isinstance(lines, (list, tuple)):
            self.lines = lines
        else:
            self.lines = (lines,)
        self.invert = invert
        self.spread = spread
        self.xspread = xspread
        self.xlim = xlim
        self.ylim = ylim
        self.xlabel = xlabel
        self.ylabel = ylabel

    def plot(self, axes):
        i = 0;
        for line in self.lines:
            line.plot(axes,
                      xoffset = self.xspread * i,
                      yoffset = self.spread * i)
            if self.xlim[0] != None: axes.set_xlim(left = self.xlim[0])
            if self.xlim[1] != None: axes.set_xlim(right = self.xlim[1])
            if self.ylim[0] != None: axes.set_ylim(bottom = self.ylim[0])
            if self.ylim[1] != None: axes.set_ylim(top = self.ylim[1])
            if self.xlabel != None: axes.set_xlabel(self.xlabel)
            if self.ylabel != None: axes.set_ylabel(self.ylabel)
            i += 1
        if self.invert: axes.invert_yaxis()
        box = axes.get_position()
        axes.set_position([box.x0, box.y0, box.width * 0.9, box.height])
        axes.legend(prop = font_props,
                    loc='upper left', bbox_to_anchor=(0.95, 1))

class Plot:
    def __init__(self, ax_spec1, ax_spec2 = None):
        self.ax_spec1 = ax_spec1
        self.ax_spec2 = ax_spec2

    def plot(self, fig, gridspec, index):
        ax1 = fig.add_subplot(gridspec[index, :])
        self.ax_spec1.plot(ax1)
        if self.ax_spec2:
            ax2 = ax1.twinx()
            self.ax_spec2.plot(ax2)

class Page:
    def __init__(self, plotspecs, filename = 'temp', title = None):
        self.plotspecs = plotspecs
        self.filename = filename
        self.title = title

    def add_line_args(self, new_args):
        for p in self.plotspecs:
            for a in (p.ax_spec1, p.ax_spec2):
                if not a: continue
                for l in a.lines:
                    l.add_args(new_args)

    def plot(self):
        nplots = len(self.plotspecs)
        fig = mpl.figure.Figure(figsize=(11, 8.5))
        canvas = FigureCanvasPdf(fig)
        if self.title: fig.suptitle(self.title)
        gs = GridSpec(nplots, 1)
        gs.update(left=0.05, right=0.94, wspace=0.05)
        for i in xrange(0, nplots):
            self.plotspecs[i].plot(fig, gs, i)
        canvas.print_figure(self.filename)

def make_plot(seriess, filename, title = None, invert = False):
    f = mpl.figure.Figure(figsize=(11, 8.5))
    canvas = FigureCanvasPdf(f)
    if title: f.suptitle(title)
    
    gs = GridSpec(len(seriess), 1)
    gs.update(left=0.05, right=0.94, wspace=0.05)
    #axess = []
    for i in range(0, len(seriess)):
        s = seriess[i]
        if isinstance(s, (list, tuple)):
            ax1 = f.add_subplot(gs[i, :])
            ax2 = ax1.twinx()
            ax2.plot(s[1].data[0], s[1].data[1],
                         color='#aaaaaa', linewidth=5.0)
            ax1.set_ylabel(s[0].get_name())
            ax1.plot(s[0].data[0], s[0].data[1], color='black')
            ax1.set_zorder(ax2.get_zorder()+1) # put ax in front of ax2
            ax1.patch.set_visible(False) # hide the 'canvas' 
            if invert:
                ax1.invert_yaxis()
                ax2.invert_yaxis()
        else:
            ax = f.add_subplot(gs[i, :])
            #axess.append(ax)
            ax.set_ylabel(s.get_name())
            ax.plot(s.data[0], s.data[1], color='black')
            if invert: ax.invert_yaxis()
    
    canvas.print_figure(filename)

def plot_2(plotdata, filename, title, use_offset = False):
    f = mpl.figure.Figure(figsize=(11, 8.5))
    canvas = FigureCanvasPdf(f)
    f.suptitle(title)
    gs = GridSpec(len(plotdata), 1)
    gs.update(left=0.05, right=0.94, wspace=0.05)
    i = 0
    offset = 0
    for newdata, refdata, invert, series_no in plotdata:
        ax1 = f.add_subplot(gs[i, :])
        ax2 = ax1.twinx()
        data = newdata.match.rate().data
        ax2.plot(data[0], data[1], color='#e0b040', linewidth=2.0,
                 linestyle = '-', marker='+', markeredgewidth=2.0)
        ax2max = ax2.get_ylim()[1]
        ax2.set_ylim([0, ax2max * 2])
        ax1.set_ylabel(newdata.series1[series_no].get_name())
        data = newdata.series1[series_no].data
        if use_offset:
            offset = -newdata.series1[series_no].std()*2
            if (invert): offset = -offset
        ax1.plot(refdata.data[0], refdata.data[1]+offset, linewidth=2.0,
                 color='#9090ff')
        ax1.plot(data[0], data[1], color='black', linewidth=0.75)
        ax1.set_zorder(ax2.get_zorder()+1) # put ax in front of ax2
        ax1.patch.set_visible(False) # hide the 'canvas'
        if invert: ax1.invert_yaxis()
        i = i + 1
    canvas.print_figure(filename)
    
class WarpPlotter:

    def __init__(self, nblocks, target, interval = 100,
                 live = True, pdf_file = None, scale = 1.):
        self.interval = interval
        self.lines = []
        self.live = live
        self.scale = scale
        self.pdf_file = pdf_file
        if self.pdf_file:
            self.pdf_pages = PdfPages(self.pdf_file)
        colours = ('yellow', 'red')
        plt.ion()
        self.fig = plt.figure()
        self.fg_colour = '#ffccaa'
        self.bg_colour = '#241C1C' # '#483737'
        mpl.rc('axes', edgecolor= self.fg_colour, labelcolor = self.fg_colour,
              facecolor = self.bg_colour)
        mpl.rc("font", family="VenturisSans ADF", size='14')
        mpl.rc('axes', edgecolor= self.fg_colour,
                      labelcolor = self.fg_colour,
                      facecolor = self.bg_colour)
        mpl.rc('xtick', color= self.fg_colour)
        mpl.rc('ytick', color= self.fg_colour)

        self.ax = self.fig.add_subplot(111)
        if target:
            self.ax.plot(target[0], target[1], color = 'blue',
                         lw = 12., ls = '--')
        for line in 0, 1:
            xs = range(nblocks)
            ys = range(nblocks)
            linetuple = self.ax.plot(xs, ys, color = colours[line],
                                     lw = 3.)
            self.lines.append(linetuple[0])

    def finish(self):
        self.lines.pop(1).remove()
        self.fig.canvas.draw()
        if hasattr(self, 'pdf_pages'):
            plt.savefig(self.pdf_pages,
                        facecolor = self.bg_colour, format = 'pdf')
            self.pdf_pages.close()

    def replot(self, soln_current, soln_new, step):
        if (step % self.interval): return
        for i, soln in ((0, soln_current), (1, soln_new)):
            xs, ys = soln.get_coords()
            self.lines[i].set_xdata([x * self.scale for x in xs])
            self.lines[i].set_ydata([y * self.scale for y in ys])
        self.fig.canvas.draw()
        if hasattr(self, 'pdf_pages'):
            plt.savefig(self.pdf_pages,
                        facecolor = self.bg_colour, format = 'pdf')