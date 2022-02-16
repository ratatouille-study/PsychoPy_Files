#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on February 14, 2022, at 19:35
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'ratouilleExperiment'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '', 'food group': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)

while '' in expInfo.values():
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)

if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\ACLab\\Desktop\\Ratatouille Study\\ratouilleExperiment.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Intro1"
Intro1Clock = core.Clock()
intro_1 = visual.TextStim(win=win, name='intro_1',
    text='Welcome to The Ratatouille Moment. The purpose of this study is to explore the effect of foods on emotions and homeostasis.\n\nYou will be rating each food image on a set of 3 questions. The goal is to assess the emotional value of each food item for you. \n\n\nPress [Space] to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Intro2"
Intro2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Rating the foods is time sensitive, so please be attentive to the screen. There will be a 15 second break every so often. \n\nTo answer the question, please click on the position on the slider that you would like to select.\n\n\nBefore we practice the task, we have 1 more question to ask you. Press [Space] to proceed.',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "hungerscale"
hungerscaleClock = core.Clock()
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(0.4, 0.04), pos=(0, -0.1), units=None,
    labels=("Not at all", "Extremely"), ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='White', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=0, readOnly=False)
text_4 = visual.TextStim(win=win, name='text_4',
    text='How hungry do you feel now?',
    font='Open Sans',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Intro3"
Intro3Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text="Let's start the task now. Press [Space] to start.",
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.20), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
FamQ = visual.TextStim(win=win, name='FamQ',
    text='How familiar is this food item to you?',
    font='Open Sans',
    units='height', pos=(-0.50, -0.15), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
FamSlider = visual.Slider(win=win, name='FamSlider',
    startValue=None, size=(0.4, 0.04), pos=(0.5, -0.15), units=None,
    labels=("Not at all", "Extremely"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='White', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.025,
    flip=False, depth=-2, readOnly=False)
ComfQ = visual.TextStim(win=win, name='ComfQ',
    text='Do you consider this food item to be a comfort food?',
    font='Open Sans',
    units='height', pos=(-0.40, -0.28), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
ComfSlider = visual.Slider(win=win, name='ComfSlider',
    startValue=None, size=(0.4,0.04), pos=(0.5, -0.28), units=None,
    labels=("Not at all", "Extremely"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='White', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.025,
    flip=False, depth=-4, readOnly=False)
NosQ = visual.TextStim(win=win, name='NosQ',
    text='Does this food hold any nostalgic value for you?',
    font='Open Sans',
    units='height', pos=(-0.425, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
NosSlider = visual.Slider(win=win, name='NosSlider',
    startValue=None, size=(0.4, 0.04), pos=(0.5, -0.4), units=None,
    labels=("Not at all", "Extremely"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='White', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.025,
    flip=False, depth=-6, readOnly=False)

# Initialize components for Routine "Start"
StartClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Congratulations, you have completed the practice. \n\nTo begin the experiment, press [Space].',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "Crosshair"
CrosshairClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='height', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.20), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
FamQ = visual.TextStim(win=win, name='FamQ',
    text='How familiar is this food item to you?',
    font='Open Sans',
    units='height', pos=(-0.50, -0.15), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
FamSlider = visual.Slider(win=win, name='FamSlider',
    startValue=None, size=(0.4, 0.04), pos=(0.5, -0.15), units=None,
    labels=("Not at all", "Extremely"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='White', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.025,
    flip=False, depth=-2, readOnly=False)
ComfQ = visual.TextStim(win=win, name='ComfQ',
    text='Do you consider this food item to be a comfort food?',
    font='Open Sans',
    units='height', pos=(-0.40, -0.28), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
ComfSlider = visual.Slider(win=win, name='ComfSlider',
    startValue=None, size=(0.4,0.04), pos=(0.5, -0.28), units=None,
    labels=("Not at all", "Extremely"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='White', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.025,
    flip=False, depth=-4, readOnly=False)
NosQ = visual.TextStim(win=win, name='NosQ',
    text='Does this food hold any nostalgic value for you?',
    font='Open Sans',
    units='height', pos=(-0.425, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
NosSlider = visual.Slider(win=win, name='NosSlider',
    startValue=None, size=(0.4, 0.04), pos=(0.5, -0.4), units=None,
    labels=("Not at all", "Extremely"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='White', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.025,
    flip=False, depth=-6, readOnly=False)

# Initialize components for Routine "hungerscale"
hungerscaleClock = core.Clock()
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(0.4, 0.04), pos=(0, -0.1), units=None,
    labels=("Not at all", "Extremely"), ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='White', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, depth=0, readOnly=False)
text_4 = visual.TextStim(win=win, name='text_4',
    text='How hungry do you feel now?',
    font='Open Sans',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end"
endClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Thank you for participating in this experiment. You will receive your SONA credits soon.\n\nPress [Space] to exit.',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Intro1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Intro1Components = [intro_1, key_resp]
for thisComponent in Intro1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Intro1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro1"-------
while continueRoutine:
    # get current time
    t = Intro1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Intro1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_1* updates
    if intro_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_1.frameNStart = frameN  # exact frame index
        intro_1.tStart = t  # local t and not account for scr refresh
        intro_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_1, 'tStartRefresh')  # time at next scr refresh
        intro_1.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro1"-------
for thisComponent in Intro1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intro_1.started', intro_1.tStartRefresh)
thisExp.addData('intro_1.stopped', intro_1.tStopRefresh)
# the Routine "Intro1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Intro2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
Intro2Components = [text_2, key_resp_2]
for thisComponent in Intro2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Intro2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro2"-------
while continueRoutine:
    # get current time
    t = Intro2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Intro2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro2"-------
for thisComponent in Intro2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Intro2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "hungerscale"-------
continueRoutine = True

#slider has no tick marks
for i, line in enumerate(slider.tickLines.sizes):
    if i not in [0,9]:  # Where 0 and 10 are your first and last tick locations
        slider.tickLines.sizes[i][1] = 0
slider.tickLines._needVertexUpdate = True

#adjust slider red marker
slider.marker.size = (.03, .03)

# update component parameters for each repeat
slider.reset()
# keep track of which components have finished
hungerscaleComponents = [slider, text_4]
for thisComponent in hungerscaleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
hungerscaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "hungerscale"-------
while continueRoutine:
    # get current time
    t = hungerscaleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=hungerscaleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *slider* updates
    if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider.frameNStart = frameN  # exact frame index
        slider.tStart = t  # local t and not account for scr refresh
        slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
        slider.setAutoDraw(True)
    
    # Check slider for response to end routine
    if slider.getRating() is not None and slider.status == STARTED:
        continueRoutine = False
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in hungerscaleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "hungerscale"-------
for thisComponent in hungerscaleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('slider.response', slider.getRating())
thisExp.addData('slider.rt', slider.getRT())
thisExp.addData('slider.started', slider.tStartRefresh)
thisExp.addData('slider.stopped', slider.tStopRefresh)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# the Routine "hungerscale" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Intro3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
Intro3Components = [text_5, key_resp_4]
for thisComponent in Intro3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Intro3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro3"-------
while continueRoutine:
    # get current time
    t = Intro3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Intro3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Intro3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro3"-------
for thisComponent in Intro3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "Intro3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
demo_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('demoImageList.xlsx', selection='0:3'),
    seed=None, name='demo_trials')
thisExp.addLoop(demo_trials)  # add the loop to the experiment
thisDemo_trial = demo_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDemo_trial.rgb)
if thisDemo_trial != None:
    for paramName in thisDemo_trial:
        exec('{} = thisDemo_trial[paramName]'.format(paramName))

for thisDemo_trial in demo_trials:
    currentLoop = demo_trials
    # abbreviate parameter names if possible (e.g. rgb = thisDemo_trial.rgb)
    if thisDemo_trial != None:
        for paramName in thisDemo_trial:
            exec('{} = thisDemo_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    
    #adjust slider red marker
    FamSlider.marker.size = (.03, .03)
    ComfSlider.marker.size = (.03, .03)
    NosSlider.marker.size = (.03, .03)
    
    # update component parameters for each repeat
    image.setImage(ImageFile)
    FamSlider.reset()
    ComfSlider.reset()
    NosSlider.reset()
    
    # keep track of which components have finished
    trialComponents = [image, FamQ, FamSlider, ComfQ, ComfSlider, NosQ, NosSlider]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *FamQ* updates
        if FamQ.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            FamQ.frameNStart = frameN  # exact frame index
            FamQ.tStart = t  # local t and not account for scr refresh
            FamQ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FamQ, 'tStartRefresh')  # time at next scr refresh
            FamQ.setAutoDraw(True)
        if FamQ.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FamQ.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                FamQ.tStop = t  # not accounting for scr refresh
                FamQ.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FamQ, 'tStopRefresh')  # time at next scr refresh
                FamQ.setAutoDraw(False)
        
        # *FamSlider* updates
        if FamSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FamSlider.frameNStart = frameN  # exact frame index
            FamSlider.tStart = t  # local t and not account for scr refresh
            FamSlider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FamSlider, 'tStartRefresh')  # time at next scr refresh
            FamSlider.setAutoDraw(True)
        if FamSlider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FamSlider.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                FamSlider.tStop = t  # not accounting for scr refresh
                FamSlider.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FamSlider, 'tStopRefresh')  # time at next scr refresh
                FamSlider.setAutoDraw(False)
        
        # *ComfQ* updates
        if ComfQ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ComfQ.frameNStart = frameN  # exact frame index
            ComfQ.tStart = t  # local t and not account for scr refresh
            ComfQ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ComfQ, 'tStartRefresh')  # time at next scr refresh
            ComfQ.setAutoDraw(True)
        if ComfQ.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ComfQ.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                ComfQ.tStop = t  # not accounting for scr refresh
                ComfQ.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ComfQ, 'tStopRefresh')  # time at next scr refresh
                ComfQ.setAutoDraw(False)
        
        # *ComfSlider* updates
        if ComfSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ComfSlider.frameNStart = frameN  # exact frame index
            ComfSlider.tStart = t  # local t and not account for scr refresh
            ComfSlider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ComfSlider, 'tStartRefresh')  # time at next scr refresh
            ComfSlider.setAutoDraw(True)
        if ComfSlider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ComfSlider.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                ComfSlider.tStop = t  # not accounting for scr refresh
                ComfSlider.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ComfSlider, 'tStopRefresh')  # time at next scr refresh
                ComfSlider.setAutoDraw(False)
        
        # *NosQ* updates
        if NosQ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NosQ.frameNStart = frameN  # exact frame index
            NosQ.tStart = t  # local t and not account for scr refresh
            NosQ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NosQ, 'tStartRefresh')  # time at next scr refresh
            NosQ.setAutoDraw(True)
        if NosQ.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NosQ.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                NosQ.tStop = t  # not accounting for scr refresh
                NosQ.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NosQ, 'tStopRefresh')  # time at next scr refresh
                NosQ.setAutoDraw(False)
        
        # *NosSlider* updates
        if NosSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NosSlider.frameNStart = frameN  # exact frame index
            NosSlider.tStart = t  # local t and not account for scr refresh
            NosSlider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NosSlider, 'tStartRefresh')  # time at next scr refresh
            NosSlider.setAutoDraw(True)
        if NosSlider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NosSlider.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                NosSlider.tStop = t  # not accounting for scr refresh
                NosSlider.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NosSlider, 'tStopRefresh')  # time at next scr refresh
                NosSlider.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    demo_trials.addData('image.started', image.tStartRefresh)
    demo_trials.addData('image.stopped', image.tStopRefresh)
    demo_trials.addData('FamQ.started', FamQ.tStartRefresh)
    demo_trials.addData('FamQ.stopped', FamQ.tStopRefresh)
    demo_trials.addData('FamSlider.response', FamSlider.getRating())
    demo_trials.addData('FamSlider.rt', FamSlider.getRT())
    demo_trials.addData('FamSlider.started', FamSlider.tStartRefresh)
    demo_trials.addData('FamSlider.stopped', FamSlider.tStopRefresh)
    demo_trials.addData('ComfQ.started', ComfQ.tStartRefresh)
    demo_trials.addData('ComfQ.stopped', ComfQ.tStopRefresh)
    demo_trials.addData('ComfSlider.response', ComfSlider.getRating())
    demo_trials.addData('ComfSlider.rt', ComfSlider.getRT())
    demo_trials.addData('ComfSlider.started', ComfSlider.tStartRefresh)
    demo_trials.addData('ComfSlider.stopped', ComfSlider.tStopRefresh)
    demo_trials.addData('NosQ.started', NosQ.tStartRefresh)
    demo_trials.addData('NosQ.stopped', NosQ.tStopRefresh)
    demo_trials.addData('NosSlider.response', NosSlider.getRating())
    demo_trials.addData('NosSlider.rt', NosSlider.getRT())
    demo_trials.addData('NosSlider.started', NosSlider.tStartRefresh)
    demo_trials.addData('NosSlider.stopped', NosSlider.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'demo_trials'


# ------Prepare to start Routine "Start"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
StartComponents = [text_3, key_resp_3]
for thisComponent in StartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Start"-------
while continueRoutine:
    # get current time
    t = StartClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start"-------
for thisComponent in StartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "Start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('C:\\Users\\ACLab\\Desktop\\Ratatouille Study\\imageList.xlsx', selection='0:5'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Crosshair"-------
    continueRoutine = False
    if trials.thisTrialN % 20 == 0 and trials.thisTrialN > 0:
        continueRoutine = True
    routineTimer.add(15.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    CrosshairComponents = [text]
    for thisComponent in CrosshairComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CrosshairClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Crosshair"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CrosshairClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CrosshairClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CrosshairComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Crosshair"-------
    for thisComponent in CrosshairComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    FamSlider.reset()
    ComfSlider.reset()
    NosSlider.reset()
    # keep track of which components have finished
    trialComponents = [image, FamQ, FamSlider, ComfQ, ComfSlider, NosQ, NosSlider]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *FamQ* updates
        if FamQ.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            FamQ.frameNStart = frameN  # exact frame index
            FamQ.tStart = t  # local t and not account for scr refresh
            FamQ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FamQ, 'tStartRefresh')  # time at next scr refresh
            FamQ.setAutoDraw(True)
        if FamQ.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FamQ.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                FamQ.tStop = t  # not accounting for scr refresh
                FamQ.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FamQ, 'tStopRefresh')  # time at next scr refresh
                FamQ.setAutoDraw(False)
        
        # *FamSlider* updates
        if FamSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FamSlider.frameNStart = frameN  # exact frame index
            FamSlider.tStart = t  # local t and not account for scr refresh
            FamSlider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FamSlider, 'tStartRefresh')  # time at next scr refresh
            FamSlider.setAutoDraw(True)
        if FamSlider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FamSlider.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                FamSlider.tStop = t  # not accounting for scr refresh
                FamSlider.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FamSlider, 'tStopRefresh')  # time at next scr refresh
                FamSlider.setAutoDraw(False)
        
        # *ComfQ* updates
        if ComfQ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ComfQ.frameNStart = frameN  # exact frame index
            ComfQ.tStart = t  # local t and not account for scr refresh
            ComfQ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ComfQ, 'tStartRefresh')  # time at next scr refresh
            ComfQ.setAutoDraw(True)
        if ComfQ.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ComfQ.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                ComfQ.tStop = t  # not accounting for scr refresh
                ComfQ.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ComfQ, 'tStopRefresh')  # time at next scr refresh
                ComfQ.setAutoDraw(False)
        
        # *ComfSlider* updates
        if ComfSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ComfSlider.frameNStart = frameN  # exact frame index
            ComfSlider.tStart = t  # local t and not account for scr refresh
            ComfSlider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ComfSlider, 'tStartRefresh')  # time at next scr refresh
            ComfSlider.setAutoDraw(True)
        if ComfSlider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ComfSlider.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                ComfSlider.tStop = t  # not accounting for scr refresh
                ComfSlider.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ComfSlider, 'tStopRefresh')  # time at next scr refresh
                ComfSlider.setAutoDraw(False)
        
        # *NosQ* updates
        if NosQ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NosQ.frameNStart = frameN  # exact frame index
            NosQ.tStart = t  # local t and not account for scr refresh
            NosQ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NosQ, 'tStartRefresh')  # time at next scr refresh
            NosQ.setAutoDraw(True)
        if NosQ.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NosQ.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                NosQ.tStop = t  # not accounting for scr refresh
                NosQ.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NosQ, 'tStopRefresh')  # time at next scr refresh
                NosQ.setAutoDraw(False)
        
        # *NosSlider* updates
        if NosSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NosSlider.frameNStart = frameN  # exact frame index
            NosSlider.tStart = t  # local t and not account for scr refresh
            NosSlider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NosSlider, 'tStartRefresh')  # time at next scr refresh
            NosSlider.setAutoDraw(True)
        if NosSlider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NosSlider.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                NosSlider.tStop = t  # not accounting for scr refresh
                NosSlider.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NosSlider, 'tStopRefresh')  # time at next scr refresh
                NosSlider.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    trials.addData('FamQ.started', FamQ.tStartRefresh)
    trials.addData('FamQ.stopped', FamQ.tStopRefresh)
    trials.addData('FamSlider.response', FamSlider.getRating())
    trials.addData('FamSlider.rt', FamSlider.getRT())
    trials.addData('FamSlider.started', FamSlider.tStartRefresh)
    trials.addData('FamSlider.stopped', FamSlider.tStopRefresh)
    trials.addData('ComfQ.started', ComfQ.tStartRefresh)
    trials.addData('ComfQ.stopped', ComfQ.tStopRefresh)
    trials.addData('ComfSlider.response', ComfSlider.getRating())
    trials.addData('ComfSlider.rt', ComfSlider.getRT())
    trials.addData('ComfSlider.started', ComfSlider.tStartRefresh)
    trials.addData('ComfSlider.stopped', ComfSlider.tStopRefresh)
    trials.addData('NosQ.started', NosQ.tStartRefresh)
    trials.addData('NosQ.stopped', NosQ.tStopRefresh)
    trials.addData('NosSlider.response', NosSlider.getRating())
    trials.addData('NosSlider.rt', NosSlider.getRT())
    trials.addData('NosSlider.started', NosSlider.tStartRefresh)
    trials.addData('NosSlider.stopped', NosSlider.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "hungerscale"-------
continueRoutine = True

# update component parameters for each repeat
slider.reset()
# keep track of which components have finished
hungerscaleComponents = [slider, text_4]
for thisComponent in hungerscaleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
hungerscaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "hungerscale"-------
while continueRoutine:
    # get current time
    t = hungerscaleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=hungerscaleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *slider* updates
    if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider.frameNStart = frameN  # exact frame index
        slider.tStart = t  # local t and not account for scr refresh
        slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
        slider.setAutoDraw(True)
    
    # Check slider for response to end routine
    if slider.getRating() is not None and slider.status == STARTED:
        continueRoutine = False
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in hungerscaleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "hungerscale"-------
for thisComponent in hungerscaleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('slider.response', slider.getRating())
thisExp.addData('slider.rt', slider.getRT())
thisExp.addData('slider.started', slider.tStartRefresh)
thisExp.addData('slider.stopped', slider.tStopRefresh)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# the Routine "hungerscale" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
endComponents = [text_6, key_resp_5]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
