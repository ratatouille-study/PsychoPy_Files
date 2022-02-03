#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on January 25, 2022, at 15:14
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
expInfo = {'participant': '', 'session': '001'}
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
    originPath='C:\\Experiment\\ratouilleExperiment_lastrun.py',
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
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='-1.0000, -1.0000, -1.0000', colorSpace='rgb',
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

# Initialize components for Routine "Introduction"
IntroductionClock = core.Clock()
intro = visual.TextStim(win=win, name='intro',
    text='Welcome to The Ratatouille Moment. The purpose of this study is to explore the effect of foods on emotions and homeostasis.\n\nYou will be rating each food image on a set of 3 questions on a scale of 1-7. The goal is to assess the emotional value of each food item for you. Rating the foods is time sensitive, so please be attentive to the screen. There will be a 15 second break every so often.\n\nPress [Space] to start.',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

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
    ori=0.0, pos=(0, 0.26), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
FamQ = visual.TextStim(win=win, name='FamQ',
    text='How familiar is this food item to you?',
    font='Open Sans',
    units='height', pos=(-0.50, -0.025), height=0.045, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
FamSlider = visual.Slider(win=win, name='FamSlider',
    startValue=None, size=(0.6, 0.06), pos=(0.5, -0.025), units=None,
    labels=("Not at all", "Extremely"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='White', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.035,
    flip=False, depth=-2, readOnly=False)
ComfQ = visual.TextStim(win=win, name='ComfQ',
    text='Do you consider this food item to be a comfort food?',
    font='Open Sans',
    units='height', pos=(-0.40, -0.24), height=0.045, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
ComfSlider = visual.Slider(win=win, name='ComfSlider',
    startValue=None, size=(0.6,0.06), pos=(0.5, -0.22), units=None,
    labels=("Not at all", "Extremely"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='White', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.035,
    flip=False, depth=-4, readOnly=False)
NosQ = visual.TextStim(win=win, name='NosQ',
    text='Does this food hold any nostalgic value for you?',
    font='Open Sans',
    units='height', pos=(-0.39, -0.4), height=0.045, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
NosSlider = visual.Slider(win=win, name='NosSlider',
    startValue=None, size=(0.6,0.06), pos=(0.5, -0.4), units=None,
    labels=("Not at all", "Extremely"), ticks=(1, 2, 3, 4, 5, 6, 7), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='White', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.035,
    flip=False, depth=-6, readOnly=False)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Introduction"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
IntroductionComponents = [intro, key_resp]
for thisComponent in IntroductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Introduction"-------
while continueRoutine:
    # get current time
    t = IntroductionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroductionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro* updates
    if intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro.frameNStart = frameN  # exact frame index
        intro.tStart = t  # local t and not account for scr refresh
        intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro, 'tStartRefresh')  # time at next scr refresh
        intro.setAutoDraw(True)
    
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
    for thisComponent in IntroductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Introduction"-------
for thisComponent in IntroductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intro.started', intro.tStartRefresh)
thisExp.addData('intro.stopped', intro.tStopRefresh)
# the Routine "Introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('C:/Experiment/imageList.xlsx', selection='0:221'),
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
    routineTimer.add(8.000000)
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
            if tThisFlipGlobal > image.tStartRefresh + 8-frameTolerance:
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
            if tThisFlipGlobal > FamQ.tStartRefresh + 8-frameTolerance:
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
            if tThisFlipGlobal > FamSlider.tStartRefresh + 8-frameTolerance:
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
            if tThisFlipGlobal > ComfQ.tStartRefresh + 8-frameTolerance:
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
            if tThisFlipGlobal > ComfSlider.tStartRefresh + 8-frameTolerance:
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
            if tThisFlipGlobal > NosQ.tStartRefresh + 8-frameTolerance:
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
            if tThisFlipGlobal > NosSlider.tStartRefresh + 8-frameTolerance:
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
