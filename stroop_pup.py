#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Февраль 21, 2022, at 14:14
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
expName = 'stroop_pup'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\aleks\\OneDrive\\Рабочий стол\\stroop_pup.py',
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
    size=[1440, 960], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text_instruction = visual.TextStim(win=win, name='text_instruction',
    text='Hello, smart guy!\nChoose the color of the word and press corresponding key\nIgnore the word\n\nr = red\nb = blue\ng = green\ny = yellow',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
response_mouse = event.Mouse(win=win)
x, y = [None, None]
response_mouse.mouseClock = core.Clock()

# Initialize components for Routine "long_fixation_cross"
long_fixation_crossClock = core.Clock()
text_long_cross = visual.TextStim(win=win, name='text_long_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "stimuli"
stimuliClock = core.Clock()
figure_rectangle = visual.Rect(
    win=win, name='figure_rectangle',
    width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
    ori=0.0, pos=(0.72, 0.47),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
text_word = visual.TextStim(win=win, name='text_word',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
response_keybord = keyboard.Keyboard()

# Initialize components for Routine "short_fixation_cross"
short_fixation_crossClock = core.Clock()
text_short_cross = visual.TextStim(win=win, name='text_short_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Thanks"
ThanksClock = core.Clock()
text_thanks = visual.TextStim(win=win, name='text_thanks',
    text='Thanks!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
win.color = 'green'
# setup some python lists for storing info about the response_mouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructionsComponents = [text_instruction, response_mouse]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instruction* updates
    if text_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instruction.frameNStart = frameN  # exact frame index
        text_instruction.tStart = t  # local t and not account for scr refresh
        text_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instruction, 'tStartRefresh')  # time at next scr refresh
        text_instruction.setAutoDraw(True)
    # *response_mouse* updates
    if response_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        response_mouse.frameNStart = frameN  # exact frame index
        response_mouse.tStart = t  # local t and not account for scr refresh
        response_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(response_mouse, 'tStartRefresh')  # time at next scr refresh
        response_mouse.status = STARTED
        response_mouse.mouseClock.reset()
        prevButtonState = response_mouse.getPressed()  # if button is down already this ISN'T a new click
    if response_mouse.status == STARTED:  # only update if started and not finished!
        buttons = response_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # abort routine on response
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
#thisExp.addData('text_instruction.started', text_instruction.tStartRefresh)
#thisExp.addData('text_instruction.stopped', text_instruction.tStopRefresh)
win.color = 'grey'
# store data for thisExp (ExperimentHandler)
x, y = response_mouse.getPos()
buttons = response_mouse.getPressed()
#thisExp.addData('response_mouse.x', x)
#thisExp.addData('response_mouse.y', y)
#thisExp.addData('response_mouse.leftButton', buttons[0])
#thisExp.addData('response_mouse.midButton', buttons[1])
#thisExp.addData('response_mouse.rightButton', buttons[2])
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "long_fixation_cross"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
long_fixation_crossComponents = [text_long_cross]
for thisComponent in long_fixation_crossComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
long_fixation_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "long_fixation_cross"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = long_fixation_crossClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=long_fixation_crossClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_long_cross* updates
    if text_long_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_long_cross.frameNStart = frameN  # exact frame index
        text_long_cross.tStart = t  # local t and not account for scr refresh
        text_long_cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_long_cross, 'tStartRefresh')  # time at next scr refresh
        text_long_cross.setAutoDraw(True)
    if text_long_cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_long_cross.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            text_long_cross.tStop = t  # not accounting for scr refresh
            text_long_cross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_long_cross, 'tStopRefresh')  # time at next scr refresh
            text_long_cross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in long_fixation_crossComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "long_fixation_cross"-------
for thisComponent in long_fixation_crossComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
#thisExp.addData('text_long_cross.started', text_long_cross.tStartRefresh)
#thisExp.addData('text_long_cross.stopped', text_long_cross.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=10.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Книга.xlsx'),
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
    
    # ------Prepare to start Routine "stimuli"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_word.setColor(color, colorSpace='rgb')
    text_word.setText(word)
    response_keybord.keys = []
    response_keybord.rt = []
    _response_keybord_allKeys = []
    # keep track of which components have finished
    stimuliComponents = [figure_rectangle, text_word, response_keybord]
    for thisComponent in stimuliComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stimuliClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stimuli"-------
    while continueRoutine:
        # get current time
        t = stimuliClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stimuliClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *figure_rectangle* updates
        if figure_rectangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            figure_rectangle.frameNStart = frameN  # exact frame index
            figure_rectangle.tStart = t  # local t and not account for scr refresh
            figure_rectangle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(figure_rectangle, 'tStartRefresh')  # time at next scr refresh
            figure_rectangle.setAutoDraw(True)
        
        # *text_word* updates
        if text_word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_word.frameNStart = frameN  # exact frame index
            text_word.tStart = t  # local t and not account for scr refresh
            text_word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_word, 'tStartRefresh')  # time at next scr refresh
            text_word.setAutoDraw(True)
        
        # *response_keybord* updates
        waitOnFlip = False
        if response_keybord.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response_keybord.frameNStart = frameN  # exact frame index
            response_keybord.tStart = t  # local t and not account for scr refresh
            response_keybord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_keybord, 'tStartRefresh')  # time at next scr refresh
            response_keybord.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_keybord.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_keybord.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_keybord.status == STARTED and not waitOnFlip:
            theseKeys = response_keybord.getKeys(keyList=['r', 'g', 'y', 'b'], waitRelease=False)
            _response_keybord_allKeys.extend(theseKeys)
            if len(_response_keybord_allKeys):
                response_keybord.keys = _response_keybord_allKeys[-1].name  # just the last key pressed
                response_keybord.rt = _response_keybord_allKeys[-1].rt
                # was this correct?
                if (response_keybord.keys == str(corrAns)) or (response_keybord.keys == corrAns):
                    response_keybord.corr = 1
                else:
                    response_keybord.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimuli"-------
    for thisComponent in stimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #trials.addData('figure_rectangle.started', figure_rectangle.tStartRefresh)
    #trials.addData('figure_rectangle.stopped', figure_rectangle.tStopRefresh)
    trials.addData('Stim timestamp', text_word.tStartRefresh)
    #trials.addData('text_word.stopped', text_word.tStopRefresh)
    # check responses
    if response_keybord.keys in ['', [], None]:  # No response was made
        response_keybord.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response_keybord.corr = 1;  # correct non-response
        else:
           response_keybord.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key pressed',response_keybord.keys)
    trials.addData('is correct', response_keybord.corr)
    if response_keybord.keys != None:  # we had a response
        trials.addData('delta T', response_keybord.rt)
    trials.addData('response_keybord.started', response_keybord.tStartRefresh)
    trials.addData('response_keybord.stopped', response_keybord.tStopRefresh)
    # the Routine "stimuli" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "short_fixation_cross"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    short_fixation_crossComponents = [text_short_cross]
    for thisComponent in short_fixation_crossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    short_fixation_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "short_fixation_cross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = short_fixation_crossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=short_fixation_crossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_short_cross* updates
        if text_short_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_short_cross.frameNStart = frameN  # exact frame index
            text_short_cross.tStart = t  # local t and not account for scr refresh
            text_short_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_short_cross, 'tStartRefresh')  # time at next scr refresh
            text_short_cross.setAutoDraw(True)
        if text_short_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_short_cross.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_short_cross.tStop = t  # not accounting for scr refresh
                text_short_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_short_cross, 'tStopRefresh')  # time at next scr refresh
                text_short_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in short_fixation_crossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "short_fixation_cross"-------
    for thisComponent in short_fixation_crossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #trials.addData('text_short_cross.started', text_short_cross.tStartRefresh)
    #trials.addData('text_short_cross.stopped', text_short_cross.tStopRefresh)
    thisExp.nextEntry()
    
# completed 10.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Thanks"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
ThanksComponents = [text_thanks]
for thisComponent in ThanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ThanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ThanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ThanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_thanks* updates
    if text_thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_thanks.frameNStart = frameN  # exact frame index
        text_thanks.tStart = t  # local t and not account for scr refresh
        text_thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_thanks, 'tStartRefresh')  # time at next scr refresh
        text_thanks.setAutoDraw(True)
    if text_thanks.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_thanks.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_thanks.tStop = t  # not accounting for scr refresh
            text_thanks.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_thanks, 'tStopRefresh')  # time at next scr refresh
            text_thanks.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thanks"-------
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
#thisExp.addData('text_thanks.started', text_thanks.tStartRefresh)
#thisExp.addData('text_thanks.stopped', text_thanks.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='semicolon')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
