import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D
import matplotlib.ticker as ticker

#------------------------------------------------
#create list for label points
listLabelPoints = []
#default starting point?
point_alpha_default = 0.8
#set mouse press to none? Boolean?
mousepress = None
#set currently_dragging to false
currently_dragging = False
#set current_artist to none, is the point being dragged
current_artist = None
#set offset to 0,0
offset = [0,0]
#set n to 0
n = 0
#set line_object to none? boolean?
line_object = None

#------------------------------------------------
#define on_press, triggered by event
def on_press(event):
    #access global vaiables
    global currently_dragging
    global mousepress
    #set currently dragging true since screen was pressed
    currently_dragging = True
    #if button pressed was mouse right click, set mouseclick to right. if it was a left click, set to left click
    if event.button == 3:
        mousepress = "right"
    elif event.button == 1:
        mousepress = "left"

#------------------------------------------------
#on press release function
def on_release(event):
    #import global variables 
    global current_artist, currently_dragging
    #nobody touching screen
    current_artist = None
    currently_dragging = False

#------------------------------------------------
def on_pick(event):
    global current_artist, offset, n
    global listLabelPoints
    if current_artist is None:
        current_artist = event.artist
        if isinstance(event.artist, patches.Circle):
            x0, y0 = current_artist.center
            x1, y1 = event.mouseevent.xdata, event.mouseevent.ydata
            offset = [(x0 - x1), (y0 - y1)]
        #print("pick ", current_artist)


#------------------------------------------------
def on_motion(event):
    global current_artist, center_X, center_Y
    if not currently_dragging:
        return
    if current_artist == None:
        return
    if event.xdata == None:
        return
    dx, dy = offset
    if isinstance(current_artist, patches.Circle):
        cx, cy =  event.xdata + dx, event.ydata + dy
        #print ('x: {}, y: {}'.format(cx, cy))
        current_artist.center = cx, cy
        #print("moving", current_artist.get_label())
        xdata = list(line_object[0].get_xdata())
        ydata = list(line_object[0].get_ydata())
        for i in range(0,len(xdata)): 
            if listLabelPoints[i] == current_artist.get_label():
                xdata[i] = cx
                center_X[i] = cx
                ydata[i] = cy
                center_Y[i] = cy
                break
        line_object[0].set_data(xdata, ydata)
    plt.draw()

#------------------------------------------------
def create_points():
    global n, line_object, xValues, yValues, center_X, center_Y
    x_ticks = (maxtime-pretime)/4
    xValues = [0, pretime, x_ticks+pretime, (2*x_ticks)+pretime, (3*x_ticks)+pretime, maxtime]
    yValues = [prebar, prebar, 5, 9, 7, 3]
    center_X = xValues
    center_Y = yValues
    for i in range(6):
        if len(listLabelPoints) < 6:
            n = n+1
            newPointLabel = "point"+str(n)
            point_object = patches.Circle([xValues[i], yValues[i]], radius=.2, color='#ff8c00', fill=True, lw=3,
                    alpha=point_alpha_default, transform=ax.transData, label=newPointLabel)
            if len(listLabelPoints)>1:
                point_object.set_picker(15) 
            ax.add_patch(point_object)
            listLabelPoints.append(newPointLabel)
            if len(listLabelPoints) == 6:
                xdata = []
                ydata = []
                for p in ax.patches:
                    cx, cy = p.center
                    xdata.append(cx)
                    ydata.append(cy)
                line_object = ax.plot(xdata, ydata, alpha=0.5, c='#ff8c00', lw=2, picker=True)
                line_object[0].set_pickradius(5)
            print("plt.draw")
            plt.draw()
            print(listLabelPoints)
            #print(xValues[i])
            #print(yValues[i])
#================================================
def get_point_data():
    print(center_X, center_Y)
    return center_X, center_Y

def make_plot(brew_time, pre_time, pre_bar):
    print("making plot")
    global fig, ax, maxtime, pretime, prebar
    maxtime = brew_time
    pretime = pre_time
    prebar = pre_bar
    touch_dpi = 133
    graph_width = 800
    graph_height = 350
    fig = plt.figure(figsize = (graph_width/touch_dpi, graph_height/touch_dpi), dpi = touch_dpi, facecolor = '#04043B')
    print("figure made")
    ax  = fig.add_subplot(111)
    ax.set_facecolor('#04043B')
    ax.set_xlabel('Time (sec)')
    ax.xaxis.label.set_color('#ff8c00')
    ax.set_ylabel('Pressure (bar)')
    ax.yaxis.label.set_color('#ff8c00')
    ax.tick_params(axis = 'x', colors = '#ff8c00')
    ax.tick_params(axis = 'y', colors = '#ff8c00')
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(base=5)) 
    ax.yaxis.set_major_locator(ticker.MultipleLocator(base=1)) 
    plt.ylim(0, 10)
    title_obj = plt.title('Create Pressure Profile')
    plt.setp(title_obj, color='#ff8c00')  
    print("creating points")
    create_points()

    #fig.canvas.mpl_connect('button_press_event', on_click)
    fig.canvas.mpl_connect('button_press_event', on_press)
    fig.canvas.mpl_connect('button_release_event', on_release)
    fig.canvas.mpl_connect('pick_event', on_pick)
    fig.canvas.mpl_connect('motion_notify_event', on_motion)
    return fig
    #plt.grid(True)
    #plt.show()

#make_plot(30,8,2)
#print('done')
#get_point_data()