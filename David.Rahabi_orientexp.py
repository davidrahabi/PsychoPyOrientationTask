#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Mon Jan  6 16:43:58 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
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
psychopyVersion = '2022.2.5'
expName = 'orientexp'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
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
    originPath='/Users/davidr/Downloads/David.Rahabi_orientexp.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# --- Initialize components for Routine "Welcome_Screen" ---
Welcome_Text = visual.TextStim(win=win, name='Welcome_Text',
    text='Welcome!\n\nIn this experiment, you will see two gratings appear serially. They will be intervened by a mask. After the second grating, indicate whether the second grating was either turned more clockwise or counter clockwise in comparison to the first grating. \n\nWhen turned clockwise, press the right arrow, when turned counter clockwise, press the left arrow.\n\nPress spacebar to start the experiment.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
Welcome_Resp = keyboard.Keyboard()

# --- Initialize components for Routine "Trial1" ---
# Run 'Begin Experiment' code from Set_CW_CCW_2
myCount=0

ISI_2 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')
base_grating_2 = visual.GratingStim(
    win=win, name='base_grating_2',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-3.0)
mask1_2 = visual.GratingStim(
    win=win, name='mask1_2',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, -0.5), size=(3, 3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
mask2_2 = visual.GratingStim(
    win=win, name='mask2_2',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, 0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
mask3_2 = visual.GratingStim(
    win=win, name='mask3_2',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,-0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-6.0)
mask4_2 = visual.GratingStim(
    win=win, name='mask4_2',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-7.0)
Change_grating_2 = visual.GratingStim(
    win=win, name='Change_grating_2',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-8.0)
Trial_Resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "Triall2" ---
# Run 'Begin Experiment' code from Set_CW_CCW_4
myCountt=0
ISI_4 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_4')
base_grating_4 = visual.GratingStim(
    win=win, name='base_grating_4',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.25, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-3.0)
mask1_4 = visual.GratingStim(
    win=win, name='mask1_4',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, -0.5), size=(3, 3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
mask2_4 = visual.GratingStim(
    win=win, name='mask2_4',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, 0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
mask3_4 = visual.GratingStim(
    win=win, name='mask3_4',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,-0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-6.0)
mask4_4 = visual.GratingStim(
    win=win, name='mask4_4',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-7.0)
Change_grating_4 = visual.GratingStim(
    win=win, name='Change_grating_4',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.25, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-8.0)
Trial_Resp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "Trial3" ---
# Run 'Begin Experiment' code from Set_CW_CCW_5
myCount3=0
ISI_5 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_5')
base_grating_5 = visual.GratingStim(
    win=win, name='base_grating_5',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.05, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-3.0)
mask1_5 = visual.GratingStim(
    win=win, name='mask1_5',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, -0.5), size=(3, 3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
mask2_5 = visual.GratingStim(
    win=win, name='mask2_5',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, 0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
mask3_5 = visual.GratingStim(
    win=win, name='mask3_5',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,-0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-6.0)
mask4_5 = visual.GratingStim(
    win=win, name='mask4_5',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-7.0)
Change_grating_5 = visual.GratingStim(
    win=win, name='Change_grating_5',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.05, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-8.0)
Trial_Resp_5 = keyboard.Keyboard()

# --- Initialize components for Routine "Trial4" ---
# Run 'Begin Experiment' code from Set_CW_CCW_6
myCount4=0
ISI_6 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_6')
base_grating_6 = visual.GratingStim(
    win=win, name='base_grating_6',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-3.0)
mask1_6 = visual.GratingStim(
    win=win, name='mask1_6',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, -0.5), size=(3, 3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
mask2_6 = visual.GratingStim(
    win=win, name='mask2_6',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, 0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
mask3_6 = visual.GratingStim(
    win=win, name='mask3_6',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,-0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-6.0)
mask4_6 = visual.GratingStim(
    win=win, name='mask4_6',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-7.0)
Change_grating_6 = visual.GratingStim(
    win=win, name='Change_grating_6',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-8.0)
Trial_Resp_6 = keyboard.Keyboard()

# --- Initialize components for Routine "Trial5" ---
# Run 'Begin Experiment' code from Set_CW_CCW_7
myCount5=0
ISI_7 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_7')
base_grating_7 = visual.GratingStim(
    win=win, name='base_grating_7',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.25, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-3.0)
mask1_7 = visual.GratingStim(
    win=win, name='mask1_7',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, -0.5), size=(3, 3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
mask2_7 = visual.GratingStim(
    win=win, name='mask2_7',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, 0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
mask3_7 = visual.GratingStim(
    win=win, name='mask3_7',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,-0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-6.0)
mask4_7 = visual.GratingStim(
    win=win, name='mask4_7',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-7.0)
Change_grating_7 = visual.GratingStim(
    win=win, name='Change_grating_7',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.25, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-8.0)
Trial_Resp_7 = keyboard.Keyboard()

# --- Initialize components for Routine "Trial6" ---
# Run 'Begin Experiment' code from Set_CW_CCW_8
myCount6=0
ISI_8 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_8')
base_grating_8 = visual.GratingStim(
    win=win, name='base_grating_8',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.05, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-3.0)
mask1_8 = visual.GratingStim(
    win=win, name='mask1_8',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, -0.5), size=(3, 3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
mask2_8 = visual.GratingStim(
    win=win, name='mask2_8',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, 0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
mask3_8 = visual.GratingStim(
    win=win, name='mask3_8',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,-0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-6.0)
mask4_8 = visual.GratingStim(
    win=win, name='mask4_8',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-7.0)
Change_grating_8 = visual.GratingStim(
    win=win, name='Change_grating_8',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.05, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-8.0)
Trial_Resp_8 = keyboard.Keyboard()

# --- Initialize components for Routine "Trial7" ---
# Run 'Begin Experiment' code from Set_CW_CCW_9
myCount7=0
ISI_9 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_9')
base_grating_9 = visual.GratingStim(
    win=win, name='base_grating_9',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-3.0)
mask1_9 = visual.GratingStim(
    win=win, name='mask1_9',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, -0.5), size=(3, 3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
mask2_9 = visual.GratingStim(
    win=win, name='mask2_9',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, 0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
mask3_9 = visual.GratingStim(
    win=win, name='mask3_9',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,-0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-6.0)
mask4_9 = visual.GratingStim(
    win=win, name='mask4_9',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-7.0)
Change_grating_9 = visual.GratingStim(
    win=win, name='Change_grating_9',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-8.0)
Trial_Resp_9 = keyboard.Keyboard()

# --- Initialize components for Routine "Trial8" ---
# Run 'Begin Experiment' code from Set_CW_CCW_10
myCount8=0
ISI_10 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_10')
base_grating_10 = visual.GratingStim(
    win=win, name='base_grating_10',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.25, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-3.0)
mask1_10 = visual.GratingStim(
    win=win, name='mask1_10',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, -0.5), size=(3, 3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
mask2_10 = visual.GratingStim(
    win=win, name='mask2_10',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, 0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
mask3_10 = visual.GratingStim(
    win=win, name='mask3_10',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,-0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-6.0)
mask4_10 = visual.GratingStim(
    win=win, name='mask4_10',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-7.0)
Change_grating_10 = visual.GratingStim(
    win=win, name='Change_grating_10',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.25, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-8.0)
Trial_Resp_10 = keyboard.Keyboard()

# --- Initialize components for Routine "Trial9" ---
# Run 'Begin Experiment' code from Set_CW_CCW_11
myCount9=0
ISI_11 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_11')
base_grating_11 = visual.GratingStim(
    win=win, name='base_grating_11',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.05, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-3.0)
mask1_11 = visual.GratingStim(
    win=win, name='mask1_11',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, -0.5), size=(3, 3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
mask2_11 = visual.GratingStim(
    win=win, name='mask2_11',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, 0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
mask3_11 = visual.GratingStim(
    win=win, name='mask3_11',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,-0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-6.0)
mask4_11 = visual.GratingStim(
    win=win, name='mask4_11',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-7.0)
Change_grating_11 = visual.GratingStim(
    win=win, name='Change_grating_11',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.05, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-8.0)
Trial_Resp_11 = keyboard.Keyboard()

# --- Initialize components for Routine "Trial" ---
# Run 'Begin Experiment' code from Set_CW_CCW
myCount11=0
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
base_grating = visual.GratingStim(
    win=win, name='base_grating',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-3.0)
mask1 = visual.GratingStim(
    win=win, name='mask1',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, -0.5), size=(3, 3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
mask2 = visual.GratingStim(
    win=win, name='mask2',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, 0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
mask3 = visual.GratingStim(
    win=win, name='mask3',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,-0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-6.0)
mask4 = visual.GratingStim(
    win=win, name='mask4',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-7.0)
Change_grating = visual.GratingStim(
    win=win, name='Change_grating',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-8.0)
Trial_Resp = keyboard.Keyboard()

# --- Initialize components for Routine "Trial_11" ---
# Run 'Begin Experiment' code from Set_CW_CCW_3
myCount12=0
ISI_3 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_3')
base_grating_3 = visual.GratingStim(
    win=win, name='base_grating_3',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.25, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-3.0)
mask1_3 = visual.GratingStim(
    win=win, name='mask1_3',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, -0.5), size=(3, 3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
mask2_3 = visual.GratingStim(
    win=win, name='mask2_3',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, 0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
mask3_3 = visual.GratingStim(
    win=win, name='mask3_3',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,-0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-6.0)
mask4_3 = visual.GratingStim(
    win=win, name='mask4_3',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-7.0)
Change_grating_3 = visual.GratingStim(
    win=win, name='Change_grating_3',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=0.25, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-8.0)
Trial_Resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "Trial12" ---
# Run 'Begin Experiment' code from Set_CW_CCW_12
myCount13=0
ISI_12 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_12')
base_grating_12 = visual.GratingStim(
    win=win, name='base_grating_12',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.05, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-3.0)
mask1_12 = visual.GratingStim(
    win=win, name='mask1_12',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, -0.5), size=(3, 3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
mask2_12 = visual.GratingStim(
    win=win, name='mask2_12',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-0.5, 0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
mask3_12 = visual.GratingStim(
    win=win, name='mask3_12',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,-0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-6.0)
mask4_12 = visual.GratingStim(
    win=win, name='mask4_12',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0.5,0.5), size=(3,3), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=1.0, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-7.0)
Change_grating_12 = visual.GratingStim(
    win=win, name='Change_grating_12',units='cm', 
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, 0), size=(4,4), sf=3.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=0.05, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-8.0)
Trial_Resp_12 = keyboard.Keyboard()

# --- Initialize components for Routine "Thank_You" ---
Thank_Yo = visual.TextStim(win=win, name='Thank_Yo',
    text='Thank you for participating!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome_Screen" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Welcome_Resp.keys = []
Welcome_Resp.rt = []
_Welcome_Resp_allKeys = []
# keep track of which components have finished
Welcome_ScreenComponents = [Welcome_Text, Welcome_Resp]
for thisComponent in Welcome_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome_Screen" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome_Text* updates
    if Welcome_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome_Text.frameNStart = frameN  # exact frame index
        Welcome_Text.tStart = t  # local t and not account for scr refresh
        Welcome_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome_Text, 'tStartRefresh')  # time at next scr refresh
        Welcome_Text.setAutoDraw(True)
    
    # *Welcome_Resp* updates
    waitOnFlip = False
    if Welcome_Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome_Resp.frameNStart = frameN  # exact frame index
        Welcome_Resp.tStart = t  # local t and not account for scr refresh
        Welcome_Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome_Resp, 'tStartRefresh')  # time at next scr refresh
        Welcome_Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Welcome_Resp.clock.reset)  # t=0 on next screen flip
    if Welcome_Resp.status == STARTED and not waitOnFlip:
        theseKeys = Welcome_Resp.getKeys(keyList=['space'], waitRelease=False)
        _Welcome_Resp_allKeys.extend(theseKeys)
        if len(_Welcome_Resp_allKeys):
            Welcome_Resp.keys = _Welcome_Resp_allKeys[-1].name  # just the last key pressed
            Welcome_Resp.rt = _Welcome_Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome_Screen" ---
for thisComponent in Welcome_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Welcome_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of trials etc
conditions = data.importConditions('Staircond.xlsx')
trials = data.MultiStairHandler(stairType='simple', name='trials',
    nTrials=1.0,
    conditions=conditions,
    method='random',
    originPath=-1)
thisExp.addLoop(trials)  # add the loop to the experiment
# initialise values for first condition
level = trials._nextIntensity  # initialise some vals
condition = trials.currentStaircase.condition

for level, condition in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
    for paramName in condition:
        exec(paramName + '= condition[paramName]')
    
    # --- Prepare to start Routine "Trial1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Set_CW_CCW_2
    myCount = myCount + 1
    if myCount == 10:
        trials.finished = True
    if random() > 0.5:
        Ori_Grat=level #positive so CW
        CorrectAns='right'
        
    else:
        Ori_Grat= - level #negative do ccw
        CorrectAns='left'
    # Run 'Begin Routine' code from Set_Mask_Orientations_2
    listnames=[]
    for x in range(1,5):
        listnames.append("maskorient" +str(x))
        print(listnames)
        
    for y in range(0,4):
        exec("%s=%d" % (listnames[y], random()*360))
        
    
    base_grating_2.setOri(0.0)
    mask1_2.setOri(maskorient1)
    mask2_2.setOri(maskorient2)
    mask3_2.setOri(maskorient3)
    mask4_2.setOri(maskorient4)
    Change_grating_2.setOri(Ori_Grat)
    Trial_Resp_2.keys = []
    Trial_Resp_2.rt = []
    _Trial_Resp_2_allKeys = []
    # keep track of which components have finished
    Trial1Components = [ISI_2, base_grating_2, mask1_2, mask2_2, mask3_2, mask4_2, Change_grating_2, Trial_Resp_2]
    for thisComponent in Trial1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Trial1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *base_grating_2* updates
        if base_grating_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            base_grating_2.frameNStart = frameN  # exact frame index
            base_grating_2.tStart = t  # local t and not account for scr refresh
            base_grating_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(base_grating_2, 'tStartRefresh')  # time at next scr refresh
            base_grating_2.setAutoDraw(True)
        if base_grating_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > base_grating_2.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                base_grating_2.tStop = t  # not accounting for scr refresh
                base_grating_2.frameNStop = frameN  # exact frame index
                base_grating_2.setAutoDraw(False)
        
        # *mask1_2* updates
        if mask1_2.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask1_2.frameNStart = frameN  # exact frame index
            mask1_2.tStart = t  # local t and not account for scr refresh
            mask1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask1_2, 'tStartRefresh')  # time at next scr refresh
            mask1_2.setAutoDraw(True)
        if mask1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask1_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask1_2.tStop = t  # not accounting for scr refresh
                mask1_2.frameNStop = frameN  # exact frame index
                mask1_2.setAutoDraw(False)
        
        # *mask2_2* updates
        if mask2_2.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask2_2.frameNStart = frameN  # exact frame index
            mask2_2.tStart = t  # local t and not account for scr refresh
            mask2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask2_2, 'tStartRefresh')  # time at next scr refresh
            mask2_2.setAutoDraw(True)
        if mask2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask2_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask2_2.tStop = t  # not accounting for scr refresh
                mask2_2.frameNStop = frameN  # exact frame index
                mask2_2.setAutoDraw(False)
        
        # *mask3_2* updates
        if mask3_2.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask3_2.frameNStart = frameN  # exact frame index
            mask3_2.tStart = t  # local t and not account for scr refresh
            mask3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask3_2, 'tStartRefresh')  # time at next scr refresh
            mask3_2.setAutoDraw(True)
        if mask3_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask3_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask3_2.tStop = t  # not accounting for scr refresh
                mask3_2.frameNStop = frameN  # exact frame index
                mask3_2.setAutoDraw(False)
        
        # *mask4_2* updates
        if mask4_2.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask4_2.frameNStart = frameN  # exact frame index
            mask4_2.tStart = t  # local t and not account for scr refresh
            mask4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask4_2, 'tStartRefresh')  # time at next scr refresh
            mask4_2.setAutoDraw(True)
        if mask4_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask4_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask4_2.tStop = t  # not accounting for scr refresh
                mask4_2.frameNStop = frameN  # exact frame index
                mask4_2.setAutoDraw(False)
        
        # *Change_grating_2* updates
        if Change_grating_2.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            Change_grating_2.frameNStart = frameN  # exact frame index
            Change_grating_2.tStart = t  # local t and not account for scr refresh
            Change_grating_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Change_grating_2, 'tStartRefresh')  # time at next scr refresh
            Change_grating_2.setAutoDraw(True)
        if Change_grating_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Change_grating_2.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                Change_grating_2.tStop = t  # not accounting for scr refresh
                Change_grating_2.frameNStop = frameN  # exact frame index
                Change_grating_2.setAutoDraw(False)
        
        # *Trial_Resp_2* updates
        waitOnFlip = False
        if Trial_Resp_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            Trial_Resp_2.frameNStart = frameN  # exact frame index
            Trial_Resp_2.tStart = t  # local t and not account for scr refresh
            Trial_Resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_Resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_Resp_2.started')
            Trial_Resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Trial_Resp_2.clock.reset)  # t=0 on next screen flip
        if Trial_Resp_2.status == STARTED and not waitOnFlip:
            theseKeys = Trial_Resp_2.getKeys(keyList=['left','right'], waitRelease=False)
            _Trial_Resp_2_allKeys.extend(theseKeys)
            if len(_Trial_Resp_2_allKeys):
                Trial_Resp_2.keys = _Trial_Resp_2_allKeys[0].name  # just the first key pressed
                Trial_Resp_2.rt = _Trial_Resp_2_allKeys[0].rt
                # was this correct?
                if (Trial_Resp_2.keys == str(CorrectAns)) or (Trial_Resp_2.keys == CorrectAns):
                    Trial_Resp_2.corr = 1
                else:
                    Trial_Resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *ISI_2* period
        if ISI_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_2.frameNStart = frameN  # exact frame index
            ISI_2.tStart = t  # local t and not account for scr refresh
            ISI_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_2, 'tStartRefresh')  # time at next scr refresh
            ISI_2.start(0.5)
        elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
            ISI_2.complete()  # finish the static period
            ISI_2.tStop = ISI_2.tStart + 0.5  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial1" ---
    for thisComponent in Trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from Set_CW_CCW_2
    
            
    # check responses
    if Trial_Resp_2.keys in ['', [], None]:  # No response was made
        Trial_Resp_2.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Trial_Resp_2.corr = 1;  # correct non-response
        else:
           Trial_Resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (MultiStairHandler)
    trials.addResponse(Trial_Resp_2.corr, level)
    trials.addOtherData('Trial_Resp_2.rt', Trial_Resp_2.rt)
    # the Routine "Trial1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# all staircases completed


# set up handler to look after randomisation of trials etc
conditions = data.importConditions('Staircond.xlsx')
trials_3 = data.MultiStairHandler(stairType='simple', name='trials_3',
    nTrials=1.0,
    conditions=conditions,
    method='random',
    originPath=-1)
thisExp.addLoop(trials_3)  # add the loop to the experiment
# initialise values for first condition
level = trials_3._nextIntensity  # initialise some vals
condition = trials_3.currentStaircase.condition

for level, condition in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
    for paramName in condition:
        exec(paramName + '= condition[paramName]')
    
    # --- Prepare to start Routine "Triall2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Set_CW_CCW_4
    myCountt = myCountt + 1
    if myCountt == 10:
        trials_3.finished = True
    if random() > 0.5:
        Ori_Grat=level #positive so CW
        CorrectAns='right'
        
    else:
        Ori_Grat= - level #negative do ccw
        CorrectAns='left'
    # Run 'Begin Routine' code from Set_Mask_Orientations_4
    listnames=[]
    for x in range(1,5):
        listnames.append("maskorient" +str(x))
        print(listnames)
        
    for y in range(0,4):
        exec("%s=%d" % (listnames[y], random()*360))
        
    
    base_grating_4.setOri(0.0)
    mask1_4.setOri(maskorient1)
    mask2_4.setOri(maskorient2)
    mask3_4.setOri(maskorient3)
    mask4_4.setOri(maskorient4)
    Change_grating_4.setOri(Ori_Grat)
    Trial_Resp_4.keys = []
    Trial_Resp_4.rt = []
    _Trial_Resp_4_allKeys = []
    # keep track of which components have finished
    Triall2Components = [ISI_4, base_grating_4, mask1_4, mask2_4, mask3_4, mask4_4, Change_grating_4, Trial_Resp_4]
    for thisComponent in Triall2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Triall2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *base_grating_4* updates
        if base_grating_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            base_grating_4.frameNStart = frameN  # exact frame index
            base_grating_4.tStart = t  # local t and not account for scr refresh
            base_grating_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(base_grating_4, 'tStartRefresh')  # time at next scr refresh
            base_grating_4.setAutoDraw(True)
        if base_grating_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > base_grating_4.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                base_grating_4.tStop = t  # not accounting for scr refresh
                base_grating_4.frameNStop = frameN  # exact frame index
                base_grating_4.setAutoDraw(False)
        
        # *mask1_4* updates
        if mask1_4.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask1_4.frameNStart = frameN  # exact frame index
            mask1_4.tStart = t  # local t and not account for scr refresh
            mask1_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask1_4, 'tStartRefresh')  # time at next scr refresh
            mask1_4.setAutoDraw(True)
        if mask1_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask1_4.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask1_4.tStop = t  # not accounting for scr refresh
                mask1_4.frameNStop = frameN  # exact frame index
                mask1_4.setAutoDraw(False)
        
        # *mask2_4* updates
        if mask2_4.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask2_4.frameNStart = frameN  # exact frame index
            mask2_4.tStart = t  # local t and not account for scr refresh
            mask2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask2_4, 'tStartRefresh')  # time at next scr refresh
            mask2_4.setAutoDraw(True)
        if mask2_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask2_4.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask2_4.tStop = t  # not accounting for scr refresh
                mask2_4.frameNStop = frameN  # exact frame index
                mask2_4.setAutoDraw(False)
        
        # *mask3_4* updates
        if mask3_4.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask3_4.frameNStart = frameN  # exact frame index
            mask3_4.tStart = t  # local t and not account for scr refresh
            mask3_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask3_4, 'tStartRefresh')  # time at next scr refresh
            mask3_4.setAutoDraw(True)
        if mask3_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask3_4.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask3_4.tStop = t  # not accounting for scr refresh
                mask3_4.frameNStop = frameN  # exact frame index
                mask3_4.setAutoDraw(False)
        
        # *mask4_4* updates
        if mask4_4.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask4_4.frameNStart = frameN  # exact frame index
            mask4_4.tStart = t  # local t and not account for scr refresh
            mask4_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask4_4, 'tStartRefresh')  # time at next scr refresh
            mask4_4.setAutoDraw(True)
        if mask4_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask4_4.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask4_4.tStop = t  # not accounting for scr refresh
                mask4_4.frameNStop = frameN  # exact frame index
                mask4_4.setAutoDraw(False)
        
        # *Change_grating_4* updates
        if Change_grating_4.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            Change_grating_4.frameNStart = frameN  # exact frame index
            Change_grating_4.tStart = t  # local t and not account for scr refresh
            Change_grating_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Change_grating_4, 'tStartRefresh')  # time at next scr refresh
            Change_grating_4.setAutoDraw(True)
        if Change_grating_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Change_grating_4.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                Change_grating_4.tStop = t  # not accounting for scr refresh
                Change_grating_4.frameNStop = frameN  # exact frame index
                Change_grating_4.setAutoDraw(False)
        
        # *Trial_Resp_4* updates
        waitOnFlip = False
        if Trial_Resp_4.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            Trial_Resp_4.frameNStart = frameN  # exact frame index
            Trial_Resp_4.tStart = t  # local t and not account for scr refresh
            Trial_Resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_Resp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_Resp_4.started')
            Trial_Resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Trial_Resp_4.clock.reset)  # t=0 on next screen flip
        if Trial_Resp_4.status == STARTED and not waitOnFlip:
            theseKeys = Trial_Resp_4.getKeys(keyList=['left','right'], waitRelease=False)
            _Trial_Resp_4_allKeys.extend(theseKeys)
            if len(_Trial_Resp_4_allKeys):
                Trial_Resp_4.keys = _Trial_Resp_4_allKeys[0].name  # just the first key pressed
                Trial_Resp_4.rt = _Trial_Resp_4_allKeys[0].rt
                # was this correct?
                if (Trial_Resp_4.keys == str(CorrectAns)) or (Trial_Resp_4.keys == CorrectAns):
                    Trial_Resp_4.corr = 1
                else:
                    Trial_Resp_4.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *ISI_4* period
        if ISI_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_4.frameNStart = frameN  # exact frame index
            ISI_4.tStart = t  # local t and not account for scr refresh
            ISI_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_4, 'tStartRefresh')  # time at next scr refresh
            ISI_4.start(0.5)
        elif ISI_4.status == STARTED:  # one frame should pass before updating params and completing
            ISI_4.complete()  # finish the static period
            ISI_4.tStop = ISI_4.tStart + 0.5  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Triall2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Triall2" ---
    for thisComponent in Triall2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from Set_CW_CCW_4
    
            
    # check responses
    if Trial_Resp_4.keys in ['', [], None]:  # No response was made
        Trial_Resp_4.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Trial_Resp_4.corr = 1;  # correct non-response
        else:
           Trial_Resp_4.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_3 (MultiStairHandler)
    trials_3.addResponse(Trial_Resp_4.corr, level)
    trials_3.addOtherData('Trial_Resp_4.rt', Trial_Resp_4.rt)
    # the Routine "Triall2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# all staircases completed


# set up handler to look after randomisation of trials etc
conditions = data.importConditions('Staircond.xlsx')
trials_2 = data.MultiStairHandler(stairType='simple', name='trials_2',
    nTrials=1.0,
    conditions=conditions,
    method='random',
    originPath=-1)
thisExp.addLoop(trials_2)  # add the loop to the experiment
# initialise values for first condition
level = trials_2._nextIntensity  # initialise some vals
condition = trials_2.currentStaircase.condition

for level, condition in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
    for paramName in condition:
        exec(paramName + '= condition[paramName]')
    
    # --- Prepare to start Routine "Trial3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Set_CW_CCW_5
    myCount3 = myCount3 + 1
    if myCount3 == 10:
        trials_2.finished = True
    if random() > 0.5:
        Ori_Grat=level #positive so CW
        CorrectAns='right'
        
    else:
        Ori_Grat= - level #negative do ccw
        CorrectAns='left'
    # Run 'Begin Routine' code from Set_Mask_Orientations_5
    listnames=[]
    for x in range(1,5):
        listnames.append("maskorient" +str(x))
        print(listnames)
        
    for y in range(0,4):
        exec("%s=%d" % (listnames[y], random()*360))
        
    
    base_grating_5.setOri(0.0)
    mask1_5.setOri(maskorient1)
    mask2_5.setOri(maskorient2)
    mask3_5.setOri(maskorient3)
    mask4_5.setOri(maskorient4)
    Change_grating_5.setOri(Ori_Grat)
    Trial_Resp_5.keys = []
    Trial_Resp_5.rt = []
    _Trial_Resp_5_allKeys = []
    # keep track of which components have finished
    Trial3Components = [ISI_5, base_grating_5, mask1_5, mask2_5, mask3_5, mask4_5, Change_grating_5, Trial_Resp_5]
    for thisComponent in Trial3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Trial3" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *base_grating_5* updates
        if base_grating_5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            base_grating_5.frameNStart = frameN  # exact frame index
            base_grating_5.tStart = t  # local t and not account for scr refresh
            base_grating_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(base_grating_5, 'tStartRefresh')  # time at next scr refresh
            base_grating_5.setAutoDraw(True)
        if base_grating_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > base_grating_5.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                base_grating_5.tStop = t  # not accounting for scr refresh
                base_grating_5.frameNStop = frameN  # exact frame index
                base_grating_5.setAutoDraw(False)
        
        # *mask1_5* updates
        if mask1_5.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask1_5.frameNStart = frameN  # exact frame index
            mask1_5.tStart = t  # local t and not account for scr refresh
            mask1_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask1_5, 'tStartRefresh')  # time at next scr refresh
            mask1_5.setAutoDraw(True)
        if mask1_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask1_5.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask1_5.tStop = t  # not accounting for scr refresh
                mask1_5.frameNStop = frameN  # exact frame index
                mask1_5.setAutoDraw(False)
        
        # *mask2_5* updates
        if mask2_5.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask2_5.frameNStart = frameN  # exact frame index
            mask2_5.tStart = t  # local t and not account for scr refresh
            mask2_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask2_5, 'tStartRefresh')  # time at next scr refresh
            mask2_5.setAutoDraw(True)
        if mask2_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask2_5.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask2_5.tStop = t  # not accounting for scr refresh
                mask2_5.frameNStop = frameN  # exact frame index
                mask2_5.setAutoDraw(False)
        
        # *mask3_5* updates
        if mask3_5.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask3_5.frameNStart = frameN  # exact frame index
            mask3_5.tStart = t  # local t and not account for scr refresh
            mask3_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask3_5, 'tStartRefresh')  # time at next scr refresh
            mask3_5.setAutoDraw(True)
        if mask3_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask3_5.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask3_5.tStop = t  # not accounting for scr refresh
                mask3_5.frameNStop = frameN  # exact frame index
                mask3_5.setAutoDraw(False)
        
        # *mask4_5* updates
        if mask4_5.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask4_5.frameNStart = frameN  # exact frame index
            mask4_5.tStart = t  # local t and not account for scr refresh
            mask4_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask4_5, 'tStartRefresh')  # time at next scr refresh
            mask4_5.setAutoDraw(True)
        if mask4_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask4_5.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask4_5.tStop = t  # not accounting for scr refresh
                mask4_5.frameNStop = frameN  # exact frame index
                mask4_5.setAutoDraw(False)
        
        # *Change_grating_5* updates
        if Change_grating_5.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            Change_grating_5.frameNStart = frameN  # exact frame index
            Change_grating_5.tStart = t  # local t and not account for scr refresh
            Change_grating_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Change_grating_5, 'tStartRefresh')  # time at next scr refresh
            Change_grating_5.setAutoDraw(True)
        if Change_grating_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Change_grating_5.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                Change_grating_5.tStop = t  # not accounting for scr refresh
                Change_grating_5.frameNStop = frameN  # exact frame index
                Change_grating_5.setAutoDraw(False)
        
        # *Trial_Resp_5* updates
        waitOnFlip = False
        if Trial_Resp_5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            Trial_Resp_5.frameNStart = frameN  # exact frame index
            Trial_Resp_5.tStart = t  # local t and not account for scr refresh
            Trial_Resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_Resp_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_Resp_5.started')
            Trial_Resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Trial_Resp_5.clock.reset)  # t=0 on next screen flip
        if Trial_Resp_5.status == STARTED and not waitOnFlip:
            theseKeys = Trial_Resp_5.getKeys(keyList=['left','right'], waitRelease=False)
            _Trial_Resp_5_allKeys.extend(theseKeys)
            if len(_Trial_Resp_5_allKeys):
                Trial_Resp_5.keys = _Trial_Resp_5_allKeys[0].name  # just the first key pressed
                Trial_Resp_5.rt = _Trial_Resp_5_allKeys[0].rt
                # was this correct?
                if (Trial_Resp_5.keys == str(CorrectAns)) or (Trial_Resp_5.keys == CorrectAns):
                    Trial_Resp_5.corr = 1
                else:
                    Trial_Resp_5.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *ISI_5* period
        if ISI_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_5.frameNStart = frameN  # exact frame index
            ISI_5.tStart = t  # local t and not account for scr refresh
            ISI_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_5, 'tStartRefresh')  # time at next scr refresh
            ISI_5.start(0.5)
        elif ISI_5.status == STARTED:  # one frame should pass before updating params and completing
            ISI_5.complete()  # finish the static period
            ISI_5.tStop = ISI_5.tStart + 0.5  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial3" ---
    for thisComponent in Trial3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from Set_CW_CCW_5
    
            
    # check responses
    if Trial_Resp_5.keys in ['', [], None]:  # No response was made
        Trial_Resp_5.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Trial_Resp_5.corr = 1;  # correct non-response
        else:
           Trial_Resp_5.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (MultiStairHandler)
    trials_2.addResponse(Trial_Resp_5.corr, level)
    trials_2.addOtherData('Trial_Resp_5.rt', Trial_Resp_5.rt)
    # the Routine "Trial3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# all staircases completed


# set up handler to look after randomisation of trials etc
conditions = data.importConditions('Staircond.xlsx')
trials_4 = data.MultiStairHandler(stairType='simple', name='trials_4',
    nTrials=1.0,
    conditions=conditions,
    method='random',
    originPath=-1)
thisExp.addLoop(trials_4)  # add the loop to the experiment
# initialise values for first condition
level = trials_4._nextIntensity  # initialise some vals
condition = trials_4.currentStaircase.condition

for level, condition in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
    for paramName in condition:
        exec(paramName + '= condition[paramName]')
    
    # --- Prepare to start Routine "Trial4" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Set_CW_CCW_6
    myCount4 = myCount4 + 1
    if myCount4  ==10:
        trials_4.finished = True
    if random() > 0.5:
        Ori_Grat=level #positive so CW
        CorrectAns='right'
        
    else:
        Ori_Grat= - level #negative do ccw
        CorrectAns='left'
    # Run 'Begin Routine' code from Set_Mask_Orientations_6
    listnames=[]
    for x in range(1,5):
        listnames.append("maskorient" +str(x))
        print(listnames)
        
    for y in range(0,4):
        exec("%s=%d" % (listnames[y], random()*360))
        
    
    base_grating_6.setOri(45.0)
    mask1_6.setOri(maskorient1)
    mask2_6.setOri(maskorient2)
    mask3_6.setOri(maskorient3)
    mask4_6.setOri(maskorient4)
    Change_grating_6.setOri(Ori_Grat)
    Trial_Resp_6.keys = []
    Trial_Resp_6.rt = []
    _Trial_Resp_6_allKeys = []
    # keep track of which components have finished
    Trial4Components = [ISI_6, base_grating_6, mask1_6, mask2_6, mask3_6, mask4_6, Change_grating_6, Trial_Resp_6]
    for thisComponent in Trial4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Trial4" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *base_grating_6* updates
        if base_grating_6.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            base_grating_6.frameNStart = frameN  # exact frame index
            base_grating_6.tStart = t  # local t and not account for scr refresh
            base_grating_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(base_grating_6, 'tStartRefresh')  # time at next scr refresh
            base_grating_6.setAutoDraw(True)
        if base_grating_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > base_grating_6.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                base_grating_6.tStop = t  # not accounting for scr refresh
                base_grating_6.frameNStop = frameN  # exact frame index
                base_grating_6.setAutoDraw(False)
        
        # *mask1_6* updates
        if mask1_6.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask1_6.frameNStart = frameN  # exact frame index
            mask1_6.tStart = t  # local t and not account for scr refresh
            mask1_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask1_6, 'tStartRefresh')  # time at next scr refresh
            mask1_6.setAutoDraw(True)
        if mask1_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask1_6.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask1_6.tStop = t  # not accounting for scr refresh
                mask1_6.frameNStop = frameN  # exact frame index
                mask1_6.setAutoDraw(False)
        
        # *mask2_6* updates
        if mask2_6.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask2_6.frameNStart = frameN  # exact frame index
            mask2_6.tStart = t  # local t and not account for scr refresh
            mask2_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask2_6, 'tStartRefresh')  # time at next scr refresh
            mask2_6.setAutoDraw(True)
        if mask2_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask2_6.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask2_6.tStop = t  # not accounting for scr refresh
                mask2_6.frameNStop = frameN  # exact frame index
                mask2_6.setAutoDraw(False)
        
        # *mask3_6* updates
        if mask3_6.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask3_6.frameNStart = frameN  # exact frame index
            mask3_6.tStart = t  # local t and not account for scr refresh
            mask3_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask3_6, 'tStartRefresh')  # time at next scr refresh
            mask3_6.setAutoDraw(True)
        if mask3_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask3_6.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask3_6.tStop = t  # not accounting for scr refresh
                mask3_6.frameNStop = frameN  # exact frame index
                mask3_6.setAutoDraw(False)
        
        # *mask4_6* updates
        if mask4_6.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask4_6.frameNStart = frameN  # exact frame index
            mask4_6.tStart = t  # local t and not account for scr refresh
            mask4_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask4_6, 'tStartRefresh')  # time at next scr refresh
            mask4_6.setAutoDraw(True)
        if mask4_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask4_6.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask4_6.tStop = t  # not accounting for scr refresh
                mask4_6.frameNStop = frameN  # exact frame index
                mask4_6.setAutoDraw(False)
        
        # *Change_grating_6* updates
        if Change_grating_6.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            Change_grating_6.frameNStart = frameN  # exact frame index
            Change_grating_6.tStart = t  # local t and not account for scr refresh
            Change_grating_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Change_grating_6, 'tStartRefresh')  # time at next scr refresh
            Change_grating_6.setAutoDraw(True)
        if Change_grating_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Change_grating_6.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                Change_grating_6.tStop = t  # not accounting for scr refresh
                Change_grating_6.frameNStop = frameN  # exact frame index
                Change_grating_6.setAutoDraw(False)
        
        # *Trial_Resp_6* updates
        waitOnFlip = False
        if Trial_Resp_6.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            Trial_Resp_6.frameNStart = frameN  # exact frame index
            Trial_Resp_6.tStart = t  # local t and not account for scr refresh
            Trial_Resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_Resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_Resp_6.started')
            Trial_Resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Trial_Resp_6.clock.reset)  # t=0 on next screen flip
        if Trial_Resp_6.status == STARTED and not waitOnFlip:
            theseKeys = Trial_Resp_6.getKeys(keyList=['left','right'], waitRelease=False)
            _Trial_Resp_6_allKeys.extend(theseKeys)
            if len(_Trial_Resp_6_allKeys):
                Trial_Resp_6.keys = _Trial_Resp_6_allKeys[0].name  # just the first key pressed
                Trial_Resp_6.rt = _Trial_Resp_6_allKeys[0].rt
                # was this correct?
                if (Trial_Resp_6.keys == str(CorrectAns)) or (Trial_Resp_6.keys == CorrectAns):
                    Trial_Resp_6.corr = 1
                else:
                    Trial_Resp_6.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *ISI_6* period
        if ISI_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_6.frameNStart = frameN  # exact frame index
            ISI_6.tStart = t  # local t and not account for scr refresh
            ISI_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_6, 'tStartRefresh')  # time at next scr refresh
            ISI_6.start(0.5)
        elif ISI_6.status == STARTED:  # one frame should pass before updating params and completing
            ISI_6.complete()  # finish the static period
            ISI_6.tStop = ISI_6.tStart + 0.5  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial4" ---
    for thisComponent in Trial4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from Set_CW_CCW_6
    
            
    # check responses
    if Trial_Resp_6.keys in ['', [], None]:  # No response was made
        Trial_Resp_6.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Trial_Resp_6.corr = 1;  # correct non-response
        else:
           Trial_Resp_6.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_4 (MultiStairHandler)
    trials_4.addResponse(Trial_Resp_6.corr, level)
    trials_4.addOtherData('Trial_Resp_6.rt', Trial_Resp_6.rt)
    # the Routine "Trial4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# all staircases completed


# set up handler to look after randomisation of trials etc
conditions = data.importConditions('Staircond.xlsx')
trials_5 = data.MultiStairHandler(stairType='simple', name='trials_5',
    nTrials=1.0,
    conditions=conditions,
    method='random',
    originPath=-1)
thisExp.addLoop(trials_5)  # add the loop to the experiment
# initialise values for first condition
level = trials_5._nextIntensity  # initialise some vals
condition = trials_5.currentStaircase.condition

for level, condition in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
    for paramName in condition:
        exec(paramName + '= condition[paramName]')
    
    # --- Prepare to start Routine "Trial5" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Set_CW_CCW_7
    myCount5 = myCount5 + 1
    if myCount5 == 10:
        trials_5.finished = True
    if random() > 0.5:
        Ori_Grat=level #positive so CW
        CorrectAns='right'
        
    else:
        Ori_Grat= - level #negative do ccw
        CorrectAns='left'
    # Run 'Begin Routine' code from Set_Mask_Orientations_7
    listnames=[]
    for x in range(1,5):
        listnames.append("maskorient" +str(x))
        print(listnames)
        
    for y in range(0,4):
        exec("%s=%d" % (listnames[y], random()*360))
        
    
    base_grating_7.setOri(45.0)
    mask1_7.setOri(maskorient1)
    mask2_7.setOri(maskorient2)
    mask3_7.setOri(maskorient3)
    mask4_7.setOri(maskorient4)
    Change_grating_7.setOri(Ori_Grat)
    Trial_Resp_7.keys = []
    Trial_Resp_7.rt = []
    _Trial_Resp_7_allKeys = []
    # keep track of which components have finished
    Trial5Components = [ISI_7, base_grating_7, mask1_7, mask2_7, mask3_7, mask4_7, Change_grating_7, Trial_Resp_7]
    for thisComponent in Trial5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Trial5" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *base_grating_7* updates
        if base_grating_7.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            base_grating_7.frameNStart = frameN  # exact frame index
            base_grating_7.tStart = t  # local t and not account for scr refresh
            base_grating_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(base_grating_7, 'tStartRefresh')  # time at next scr refresh
            base_grating_7.setAutoDraw(True)
        if base_grating_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > base_grating_7.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                base_grating_7.tStop = t  # not accounting for scr refresh
                base_grating_7.frameNStop = frameN  # exact frame index
                base_grating_7.setAutoDraw(False)
        
        # *mask1_7* updates
        if mask1_7.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask1_7.frameNStart = frameN  # exact frame index
            mask1_7.tStart = t  # local t and not account for scr refresh
            mask1_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask1_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'mask1_7.started')
            mask1_7.setAutoDraw(True)
        if mask1_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask1_7.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask1_7.tStop = t  # not accounting for scr refresh
                mask1_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mask1_7.stopped')
                mask1_7.setAutoDraw(False)
        
        # *mask2_7* updates
        if mask2_7.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask2_7.frameNStart = frameN  # exact frame index
            mask2_7.tStart = t  # local t and not account for scr refresh
            mask2_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask2_7, 'tStartRefresh')  # time at next scr refresh
            mask2_7.setAutoDraw(True)
        if mask2_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask2_7.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask2_7.tStop = t  # not accounting for scr refresh
                mask2_7.frameNStop = frameN  # exact frame index
                mask2_7.setAutoDraw(False)
        
        # *mask3_7* updates
        if mask3_7.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask3_7.frameNStart = frameN  # exact frame index
            mask3_7.tStart = t  # local t and not account for scr refresh
            mask3_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask3_7, 'tStartRefresh')  # time at next scr refresh
            mask3_7.setAutoDraw(True)
        if mask3_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask3_7.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask3_7.tStop = t  # not accounting for scr refresh
                mask3_7.frameNStop = frameN  # exact frame index
                mask3_7.setAutoDraw(False)
        
        # *mask4_7* updates
        if mask4_7.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask4_7.frameNStart = frameN  # exact frame index
            mask4_7.tStart = t  # local t and not account for scr refresh
            mask4_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask4_7, 'tStartRefresh')  # time at next scr refresh
            mask4_7.setAutoDraw(True)
        if mask4_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask4_7.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask4_7.tStop = t  # not accounting for scr refresh
                mask4_7.frameNStop = frameN  # exact frame index
                mask4_7.setAutoDraw(False)
        
        # *Change_grating_7* updates
        if Change_grating_7.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            Change_grating_7.frameNStart = frameN  # exact frame index
            Change_grating_7.tStart = t  # local t and not account for scr refresh
            Change_grating_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Change_grating_7, 'tStartRefresh')  # time at next scr refresh
            Change_grating_7.setAutoDraw(True)
        if Change_grating_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Change_grating_7.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                Change_grating_7.tStop = t  # not accounting for scr refresh
                Change_grating_7.frameNStop = frameN  # exact frame index
                Change_grating_7.setAutoDraw(False)
        
        # *Trial_Resp_7* updates
        waitOnFlip = False
        if Trial_Resp_7.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            Trial_Resp_7.frameNStart = frameN  # exact frame index
            Trial_Resp_7.tStart = t  # local t and not account for scr refresh
            Trial_Resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_Resp_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_Resp_7.started')
            Trial_Resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Trial_Resp_7.clock.reset)  # t=0 on next screen flip
        if Trial_Resp_7.status == STARTED and not waitOnFlip:
            theseKeys = Trial_Resp_7.getKeys(keyList=['left','right'], waitRelease=False)
            _Trial_Resp_7_allKeys.extend(theseKeys)
            if len(_Trial_Resp_7_allKeys):
                Trial_Resp_7.keys = _Trial_Resp_7_allKeys[0].name  # just the first key pressed
                Trial_Resp_7.rt = _Trial_Resp_7_allKeys[0].rt
                # was this correct?
                if (Trial_Resp_7.keys == str(CorrectAns)) or (Trial_Resp_7.keys == CorrectAns):
                    Trial_Resp_7.corr = 1
                else:
                    Trial_Resp_7.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *ISI_7* period
        if ISI_7.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_7.frameNStart = frameN  # exact frame index
            ISI_7.tStart = t  # local t and not account for scr refresh
            ISI_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_7, 'tStartRefresh')  # time at next scr refresh
            ISI_7.start(0.5)
        elif ISI_7.status == STARTED:  # one frame should pass before updating params and completing
            ISI_7.complete()  # finish the static period
            ISI_7.tStop = ISI_7.tStart + 0.5  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial5" ---
    for thisComponent in Trial5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from Set_CW_CCW_7
    
            
    # check responses
    if Trial_Resp_7.keys in ['', [], None]:  # No response was made
        Trial_Resp_7.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Trial_Resp_7.corr = 1;  # correct non-response
        else:
           Trial_Resp_7.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_5 (MultiStairHandler)
    trials_5.addResponse(Trial_Resp_7.corr, level)
    trials_5.addOtherData('Trial_Resp_7.rt', Trial_Resp_7.rt)
    # the Routine "Trial5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# all staircases completed


# set up handler to look after randomisation of trials etc
conditions = data.importConditions('Staircond.xlsx')
trials_6 = data.MultiStairHandler(stairType='simple', name='trials_6',
    nTrials=50.0,
    conditions=conditions,
    method='random',
    originPath=-1)
thisExp.addLoop(trials_6)  # add the loop to the experiment
# initialise values for first condition
level = trials_6._nextIntensity  # initialise some vals
condition = trials_6.currentStaircase.condition

for level, condition in trials_6:
    currentLoop = trials_6
    # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
    for paramName in condition:
        exec(paramName + '= condition[paramName]')
    
    # --- Prepare to start Routine "Trial6" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Set_CW_CCW_8
    myCount6 = myCount6 + 1
    if myCount6 == 10:
        trials_6.finished = True
    if random() > 0.5:
        Ori_Grat=level #positive so CW
        CorrectAns='right'
        
    else:
        Ori_Grat= - level #negative do ccw
        CorrectAns='left'
    # Run 'Begin Routine' code from Set_Mask_Orientations_8
    listnames=[]
    for x in range(1,5):
        listnames.append("maskorient" +str(x))
        print(listnames)
        
    for y in range(0,4):
        exec("%s=%d" % (listnames[y], random()*360))
        
    
    base_grating_8.setOri(45.0)
    mask1_8.setOri(maskorient1)
    mask2_8.setOri(maskorient2)
    mask3_8.setOri(maskorient3)
    mask4_8.setOri(maskorient4)
    Change_grating_8.setOri(Ori_Grat)
    Trial_Resp_8.keys = []
    Trial_Resp_8.rt = []
    _Trial_Resp_8_allKeys = []
    # keep track of which components have finished
    Trial6Components = [ISI_8, base_grating_8, mask1_8, mask2_8, mask3_8, mask4_8, Change_grating_8, Trial_Resp_8]
    for thisComponent in Trial6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Trial6" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *base_grating_8* updates
        if base_grating_8.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            base_grating_8.frameNStart = frameN  # exact frame index
            base_grating_8.tStart = t  # local t and not account for scr refresh
            base_grating_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(base_grating_8, 'tStartRefresh')  # time at next scr refresh
            base_grating_8.setAutoDraw(True)
        if base_grating_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > base_grating_8.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                base_grating_8.tStop = t  # not accounting for scr refresh
                base_grating_8.frameNStop = frameN  # exact frame index
                base_grating_8.setAutoDraw(False)
        
        # *mask1_8* updates
        if mask1_8.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask1_8.frameNStart = frameN  # exact frame index
            mask1_8.tStart = t  # local t and not account for scr refresh
            mask1_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask1_8, 'tStartRefresh')  # time at next scr refresh
            mask1_8.setAutoDraw(True)
        if mask1_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask1_8.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask1_8.tStop = t  # not accounting for scr refresh
                mask1_8.frameNStop = frameN  # exact frame index
                mask1_8.setAutoDraw(False)
        
        # *mask2_8* updates
        if mask2_8.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask2_8.frameNStart = frameN  # exact frame index
            mask2_8.tStart = t  # local t and not account for scr refresh
            mask2_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask2_8, 'tStartRefresh')  # time at next scr refresh
            mask2_8.setAutoDraw(True)
        if mask2_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask2_8.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask2_8.tStop = t  # not accounting for scr refresh
                mask2_8.frameNStop = frameN  # exact frame index
                mask2_8.setAutoDraw(False)
        
        # *mask3_8* updates
        if mask3_8.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask3_8.frameNStart = frameN  # exact frame index
            mask3_8.tStart = t  # local t and not account for scr refresh
            mask3_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask3_8, 'tStartRefresh')  # time at next scr refresh
            mask3_8.setAutoDraw(True)
        if mask3_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask3_8.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask3_8.tStop = t  # not accounting for scr refresh
                mask3_8.frameNStop = frameN  # exact frame index
                mask3_8.setAutoDraw(False)
        
        # *mask4_8* updates
        if mask4_8.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask4_8.frameNStart = frameN  # exact frame index
            mask4_8.tStart = t  # local t and not account for scr refresh
            mask4_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask4_8, 'tStartRefresh')  # time at next scr refresh
            mask4_8.setAutoDraw(True)
        if mask4_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask4_8.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask4_8.tStop = t  # not accounting for scr refresh
                mask4_8.frameNStop = frameN  # exact frame index
                mask4_8.setAutoDraw(False)
        
        # *Change_grating_8* updates
        if Change_grating_8.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            Change_grating_8.frameNStart = frameN  # exact frame index
            Change_grating_8.tStart = t  # local t and not account for scr refresh
            Change_grating_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Change_grating_8, 'tStartRefresh')  # time at next scr refresh
            Change_grating_8.setAutoDraw(True)
        if Change_grating_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Change_grating_8.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                Change_grating_8.tStop = t  # not accounting for scr refresh
                Change_grating_8.frameNStop = frameN  # exact frame index
                Change_grating_8.setAutoDraw(False)
        
        # *Trial_Resp_8* updates
        waitOnFlip = False
        if Trial_Resp_8.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            Trial_Resp_8.frameNStart = frameN  # exact frame index
            Trial_Resp_8.tStart = t  # local t and not account for scr refresh
            Trial_Resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_Resp_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_Resp_8.started')
            Trial_Resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Trial_Resp_8.clock.reset)  # t=0 on next screen flip
        if Trial_Resp_8.status == STARTED and not waitOnFlip:
            theseKeys = Trial_Resp_8.getKeys(keyList=['left','right'], waitRelease=False)
            _Trial_Resp_8_allKeys.extend(theseKeys)
            if len(_Trial_Resp_8_allKeys):
                Trial_Resp_8.keys = _Trial_Resp_8_allKeys[0].name  # just the first key pressed
                Trial_Resp_8.rt = _Trial_Resp_8_allKeys[0].rt
                # was this correct?
                if (Trial_Resp_8.keys == str(CorrectAns)) or (Trial_Resp_8.keys == CorrectAns):
                    Trial_Resp_8.corr = 1
                else:
                    Trial_Resp_8.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *ISI_8* period
        if ISI_8.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_8.frameNStart = frameN  # exact frame index
            ISI_8.tStart = t  # local t and not account for scr refresh
            ISI_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_8, 'tStartRefresh')  # time at next scr refresh
            ISI_8.start(0.5)
        elif ISI_8.status == STARTED:  # one frame should pass before updating params and completing
            ISI_8.complete()  # finish the static period
            ISI_8.tStop = ISI_8.tStart + 0.5  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial6" ---
    for thisComponent in Trial6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from Set_CW_CCW_8
    
            
    # check responses
    if Trial_Resp_8.keys in ['', [], None]:  # No response was made
        Trial_Resp_8.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Trial_Resp_8.corr = 1;  # correct non-response
        else:
           Trial_Resp_8.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_6 (MultiStairHandler)
    trials_6.addResponse(Trial_Resp_8.corr, level)
    trials_6.addOtherData('Trial_Resp_8.rt', Trial_Resp_8.rt)
    # the Routine "Trial6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# all staircases completed


# set up handler to look after randomisation of trials etc
conditions = data.importConditions('Staircond.xlsx')
trials_7 = data.MultiStairHandler(stairType='simple', name='trials_7',
    nTrials=1.0,
    conditions=conditions,
    method='random',
    originPath=-1)
thisExp.addLoop(trials_7)  # add the loop to the experiment
# initialise values for first condition
level = trials_7._nextIntensity  # initialise some vals
condition = trials_7.currentStaircase.condition

for level, condition in trials_7:
    currentLoop = trials_7
    # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
    for paramName in condition:
        exec(paramName + '= condition[paramName]')
    
    # --- Prepare to start Routine "Trial7" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Set_CW_CCW_9
    myCount7 = myCount7 + 1
    if myCount7 == 10:
        trials_7.finished = True
    if random() > 0.5:
        Ori_Grat=level #positive so CW
        CorrectAns='right'
        
    else:
        Ori_Grat= - level #negative do ccw
        CorrectAns='left'
    # Run 'Begin Routine' code from Set_Mask_Orientations_9
    listnames=[]
    for x in range(1,5):
        listnames.append("maskorient" +str(x))
        print(listnames)
        
    for y in range(0,4):
        exec("%s=%d" % (listnames[y], random()*360))
        
    
    base_grating_9.setOri(90.0)
    mask1_9.setOri(maskorient1)
    mask2_9.setOri(maskorient2)
    mask3_9.setOri(maskorient3)
    mask4_9.setOri(maskorient4)
    Change_grating_9.setOri(Ori_Grat)
    Trial_Resp_9.keys = []
    Trial_Resp_9.rt = []
    _Trial_Resp_9_allKeys = []
    # keep track of which components have finished
    Trial7Components = [ISI_9, base_grating_9, mask1_9, mask2_9, mask3_9, mask4_9, Change_grating_9, Trial_Resp_9]
    for thisComponent in Trial7Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Trial7" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *base_grating_9* updates
        if base_grating_9.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            base_grating_9.frameNStart = frameN  # exact frame index
            base_grating_9.tStart = t  # local t and not account for scr refresh
            base_grating_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(base_grating_9, 'tStartRefresh')  # time at next scr refresh
            base_grating_9.setAutoDraw(True)
        if base_grating_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > base_grating_9.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                base_grating_9.tStop = t  # not accounting for scr refresh
                base_grating_9.frameNStop = frameN  # exact frame index
                base_grating_9.setAutoDraw(False)
        
        # *mask1_9* updates
        if mask1_9.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask1_9.frameNStart = frameN  # exact frame index
            mask1_9.tStart = t  # local t and not account for scr refresh
            mask1_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask1_9, 'tStartRefresh')  # time at next scr refresh
            mask1_9.setAutoDraw(True)
        if mask1_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask1_9.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask1_9.tStop = t  # not accounting for scr refresh
                mask1_9.frameNStop = frameN  # exact frame index
                mask1_9.setAutoDraw(False)
        
        # *mask2_9* updates
        if mask2_9.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask2_9.frameNStart = frameN  # exact frame index
            mask2_9.tStart = t  # local t and not account for scr refresh
            mask2_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask2_9, 'tStartRefresh')  # time at next scr refresh
            mask2_9.setAutoDraw(True)
        if mask2_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask2_9.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask2_9.tStop = t  # not accounting for scr refresh
                mask2_9.frameNStop = frameN  # exact frame index
                mask2_9.setAutoDraw(False)
        
        # *mask3_9* updates
        if mask3_9.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask3_9.frameNStart = frameN  # exact frame index
            mask3_9.tStart = t  # local t and not account for scr refresh
            mask3_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask3_9, 'tStartRefresh')  # time at next scr refresh
            mask3_9.setAutoDraw(True)
        if mask3_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask3_9.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask3_9.tStop = t  # not accounting for scr refresh
                mask3_9.frameNStop = frameN  # exact frame index
                mask3_9.setAutoDraw(False)
        
        # *mask4_9* updates
        if mask4_9.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask4_9.frameNStart = frameN  # exact frame index
            mask4_9.tStart = t  # local t and not account for scr refresh
            mask4_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask4_9, 'tStartRefresh')  # time at next scr refresh
            mask4_9.setAutoDraw(True)
        if mask4_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask4_9.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask4_9.tStop = t  # not accounting for scr refresh
                mask4_9.frameNStop = frameN  # exact frame index
                mask4_9.setAutoDraw(False)
        
        # *Change_grating_9* updates
        if Change_grating_9.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            Change_grating_9.frameNStart = frameN  # exact frame index
            Change_grating_9.tStart = t  # local t and not account for scr refresh
            Change_grating_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Change_grating_9, 'tStartRefresh')  # time at next scr refresh
            Change_grating_9.setAutoDraw(True)
        if Change_grating_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Change_grating_9.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                Change_grating_9.tStop = t  # not accounting for scr refresh
                Change_grating_9.frameNStop = frameN  # exact frame index
                Change_grating_9.setAutoDraw(False)
        
        # *Trial_Resp_9* updates
        waitOnFlip = False
        if Trial_Resp_9.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            Trial_Resp_9.frameNStart = frameN  # exact frame index
            Trial_Resp_9.tStart = t  # local t and not account for scr refresh
            Trial_Resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_Resp_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_Resp_9.started')
            Trial_Resp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Trial_Resp_9.clock.reset)  # t=0 on next screen flip
        if Trial_Resp_9.status == STARTED and not waitOnFlip:
            theseKeys = Trial_Resp_9.getKeys(keyList=['left','right'], waitRelease=False)
            _Trial_Resp_9_allKeys.extend(theseKeys)
            if len(_Trial_Resp_9_allKeys):
                Trial_Resp_9.keys = _Trial_Resp_9_allKeys[0].name  # just the first key pressed
                Trial_Resp_9.rt = _Trial_Resp_9_allKeys[0].rt
                # was this correct?
                if (Trial_Resp_9.keys == str(CorrectAns)) or (Trial_Resp_9.keys == CorrectAns):
                    Trial_Resp_9.corr = 1
                else:
                    Trial_Resp_9.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *ISI_9* period
        if ISI_9.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_9.frameNStart = frameN  # exact frame index
            ISI_9.tStart = t  # local t and not account for scr refresh
            ISI_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_9, 'tStartRefresh')  # time at next scr refresh
            ISI_9.start(0.5)
        elif ISI_9.status == STARTED:  # one frame should pass before updating params and completing
            ISI_9.complete()  # finish the static period
            ISI_9.tStop = ISI_9.tStart + 0.5  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial7" ---
    for thisComponent in Trial7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from Set_CW_CCW_9
    
            
    # check responses
    if Trial_Resp_9.keys in ['', [], None]:  # No response was made
        Trial_Resp_9.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Trial_Resp_9.corr = 1;  # correct non-response
        else:
           Trial_Resp_9.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_7 (MultiStairHandler)
    trials_7.addResponse(Trial_Resp_9.corr, level)
    trials_7.addOtherData('Trial_Resp_9.rt', Trial_Resp_9.rt)
    # the Routine "Trial7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# all staircases completed


# set up handler to look after randomisation of trials etc
conditions = data.importConditions('Staircond.xlsx')
trials_8 = data.MultiStairHandler(stairType='simple', name='trials_8',
    nTrials=1.0,
    conditions=conditions,
    method='random',
    originPath=-1)
thisExp.addLoop(trials_8)  # add the loop to the experiment
# initialise values for first condition
level = trials_8._nextIntensity  # initialise some vals
condition = trials_8.currentStaircase.condition

for level, condition in trials_8:
    currentLoop = trials_8
    # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
    for paramName in condition:
        exec(paramName + '= condition[paramName]')
    
    # --- Prepare to start Routine "Trial8" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Set_CW_CCW_10
    myCount8 = myCount8 + 1
    if myCount8 == 10:
        trials_8.finished = True
    if random() > 0.5:
        Ori_Grat=level #positive so CW
        CorrectAns='right'
        
    else:
        Ori_Grat= - level #negative do ccw
        CorrectAns='left'
    # Run 'Begin Routine' code from Set_Mask_Orientations_10
    listnames=[]
    for x in range(1,5):
        listnames.append("maskorient" +str(x))
        print(listnames)
        
    for y in range(0,4):
        exec("%s=%d" % (listnames[y], random()*360))
        
    
    base_grating_10.setOri(90.0)
    mask1_10.setOri(maskorient1)
    mask2_10.setOri(maskorient2)
    mask3_10.setOri(maskorient3)
    mask4_10.setOri(maskorient4)
    Change_grating_10.setOri(Ori_Grat)
    Trial_Resp_10.keys = []
    Trial_Resp_10.rt = []
    _Trial_Resp_10_allKeys = []
    # keep track of which components have finished
    Trial8Components = [ISI_10, base_grating_10, mask1_10, mask2_10, mask3_10, mask4_10, Change_grating_10, Trial_Resp_10]
    for thisComponent in Trial8Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Trial8" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *base_grating_10* updates
        if base_grating_10.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            base_grating_10.frameNStart = frameN  # exact frame index
            base_grating_10.tStart = t  # local t and not account for scr refresh
            base_grating_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(base_grating_10, 'tStartRefresh')  # time at next scr refresh
            base_grating_10.setAutoDraw(True)
        if base_grating_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > base_grating_10.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                base_grating_10.tStop = t  # not accounting for scr refresh
                base_grating_10.frameNStop = frameN  # exact frame index
                base_grating_10.setAutoDraw(False)
        
        # *mask1_10* updates
        if mask1_10.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask1_10.frameNStart = frameN  # exact frame index
            mask1_10.tStart = t  # local t and not account for scr refresh
            mask1_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask1_10, 'tStartRefresh')  # time at next scr refresh
            mask1_10.setAutoDraw(True)
        if mask1_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask1_10.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask1_10.tStop = t  # not accounting for scr refresh
                mask1_10.frameNStop = frameN  # exact frame index
                mask1_10.setAutoDraw(False)
        
        # *mask2_10* updates
        if mask2_10.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask2_10.frameNStart = frameN  # exact frame index
            mask2_10.tStart = t  # local t and not account for scr refresh
            mask2_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask2_10, 'tStartRefresh')  # time at next scr refresh
            mask2_10.setAutoDraw(True)
        if mask2_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask2_10.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask2_10.tStop = t  # not accounting for scr refresh
                mask2_10.frameNStop = frameN  # exact frame index
                mask2_10.setAutoDraw(False)
        
        # *mask3_10* updates
        if mask3_10.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask3_10.frameNStart = frameN  # exact frame index
            mask3_10.tStart = t  # local t and not account for scr refresh
            mask3_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask3_10, 'tStartRefresh')  # time at next scr refresh
            mask3_10.setAutoDraw(True)
        if mask3_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask3_10.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask3_10.tStop = t  # not accounting for scr refresh
                mask3_10.frameNStop = frameN  # exact frame index
                mask3_10.setAutoDraw(False)
        
        # *mask4_10* updates
        if mask4_10.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask4_10.frameNStart = frameN  # exact frame index
            mask4_10.tStart = t  # local t and not account for scr refresh
            mask4_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask4_10, 'tStartRefresh')  # time at next scr refresh
            mask4_10.setAutoDraw(True)
        if mask4_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask4_10.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask4_10.tStop = t  # not accounting for scr refresh
                mask4_10.frameNStop = frameN  # exact frame index
                mask4_10.setAutoDraw(False)
        
        # *Change_grating_10* updates
        if Change_grating_10.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            Change_grating_10.frameNStart = frameN  # exact frame index
            Change_grating_10.tStart = t  # local t and not account for scr refresh
            Change_grating_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Change_grating_10, 'tStartRefresh')  # time at next scr refresh
            Change_grating_10.setAutoDraw(True)
        if Change_grating_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Change_grating_10.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                Change_grating_10.tStop = t  # not accounting for scr refresh
                Change_grating_10.frameNStop = frameN  # exact frame index
                Change_grating_10.setAutoDraw(False)
        
        # *Trial_Resp_10* updates
        waitOnFlip = False
        if Trial_Resp_10.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            Trial_Resp_10.frameNStart = frameN  # exact frame index
            Trial_Resp_10.tStart = t  # local t and not account for scr refresh
            Trial_Resp_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_Resp_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_Resp_10.started')
            Trial_Resp_10.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Trial_Resp_10.clock.reset)  # t=0 on next screen flip
        if Trial_Resp_10.status == STARTED and not waitOnFlip:
            theseKeys = Trial_Resp_10.getKeys(keyList=['left','right'], waitRelease=False)
            _Trial_Resp_10_allKeys.extend(theseKeys)
            if len(_Trial_Resp_10_allKeys):
                Trial_Resp_10.keys = _Trial_Resp_10_allKeys[0].name  # just the first key pressed
                Trial_Resp_10.rt = _Trial_Resp_10_allKeys[0].rt
                # was this correct?
                if (Trial_Resp_10.keys == str(CorrectAns)) or (Trial_Resp_10.keys == CorrectAns):
                    Trial_Resp_10.corr = 1
                else:
                    Trial_Resp_10.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *ISI_10* period
        if ISI_10.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_10.frameNStart = frameN  # exact frame index
            ISI_10.tStart = t  # local t and not account for scr refresh
            ISI_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_10, 'tStartRefresh')  # time at next scr refresh
            ISI_10.start(0.5)
        elif ISI_10.status == STARTED:  # one frame should pass before updating params and completing
            ISI_10.complete()  # finish the static period
            ISI_10.tStop = ISI_10.tStart + 0.5  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial8" ---
    for thisComponent in Trial8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from Set_CW_CCW_10
    
            
    # check responses
    if Trial_Resp_10.keys in ['', [], None]:  # No response was made
        Trial_Resp_10.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Trial_Resp_10.corr = 1;  # correct non-response
        else:
           Trial_Resp_10.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_8 (MultiStairHandler)
    trials_8.addResponse(Trial_Resp_10.corr, level)
    trials_8.addOtherData('Trial_Resp_10.rt', Trial_Resp_10.rt)
    # the Routine "Trial8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# all staircases completed


# set up handler to look after randomisation of trials etc
conditions = data.importConditions('Staircond.xlsx')
trials_9 = data.MultiStairHandler(stairType='simple', name='trials_9',
    nTrials=1.0,
    conditions=conditions,
    method='random',
    originPath=-1)
thisExp.addLoop(trials_9)  # add the loop to the experiment
# initialise values for first condition
level = trials_9._nextIntensity  # initialise some vals
condition = trials_9.currentStaircase.condition

for level, condition in trials_9:
    currentLoop = trials_9
    # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
    for paramName in condition:
        exec(paramName + '= condition[paramName]')
    
    # --- Prepare to start Routine "Trial9" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Set_CW_CCW_11
    myCount9 = myCount9 + 1
    if myCount9 == 10:
        trials_9.finished = True
    if random() > 0.5:
        Ori_Grat=level #positive so CW
        CorrectAns='right'
        
    else:
        Ori_Grat= - level #negative do ccw
        CorrectAns='left'
    # Run 'Begin Routine' code from Set_Mask_Orientations_11
    listnames=[]
    for x in range(1,5):
        listnames.append("maskorient" +str(x))
        print(listnames)
        
    for y in range(0,4):
        exec("%s=%d" % (listnames[y], random()*360))
        
    
    base_grating_11.setOri(90.0)
    mask1_11.setOri(maskorient1)
    mask2_11.setOri(maskorient2)
    mask3_11.setOri(maskorient3)
    mask4_11.setOri(maskorient4)
    Change_grating_11.setOri(Ori_Grat)
    Trial_Resp_11.keys = []
    Trial_Resp_11.rt = []
    _Trial_Resp_11_allKeys = []
    # keep track of which components have finished
    Trial9Components = [ISI_11, base_grating_11, mask1_11, mask2_11, mask3_11, mask4_11, Change_grating_11, Trial_Resp_11]
    for thisComponent in Trial9Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Trial9" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *base_grating_11* updates
        if base_grating_11.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            base_grating_11.frameNStart = frameN  # exact frame index
            base_grating_11.tStart = t  # local t and not account for scr refresh
            base_grating_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(base_grating_11, 'tStartRefresh')  # time at next scr refresh
            base_grating_11.setAutoDraw(True)
        if base_grating_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > base_grating_11.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                base_grating_11.tStop = t  # not accounting for scr refresh
                base_grating_11.frameNStop = frameN  # exact frame index
                base_grating_11.setAutoDraw(False)
        
        # *mask1_11* updates
        if mask1_11.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask1_11.frameNStart = frameN  # exact frame index
            mask1_11.tStart = t  # local t and not account for scr refresh
            mask1_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask1_11, 'tStartRefresh')  # time at next scr refresh
            mask1_11.setAutoDraw(True)
        if mask1_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask1_11.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask1_11.tStop = t  # not accounting for scr refresh
                mask1_11.frameNStop = frameN  # exact frame index
                mask1_11.setAutoDraw(False)
        
        # *mask2_11* updates
        if mask2_11.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask2_11.frameNStart = frameN  # exact frame index
            mask2_11.tStart = t  # local t and not account for scr refresh
            mask2_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask2_11, 'tStartRefresh')  # time at next scr refresh
            mask2_11.setAutoDraw(True)
        if mask2_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask2_11.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask2_11.tStop = t  # not accounting for scr refresh
                mask2_11.frameNStop = frameN  # exact frame index
                mask2_11.setAutoDraw(False)
        
        # *mask3_11* updates
        if mask3_11.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask3_11.frameNStart = frameN  # exact frame index
            mask3_11.tStart = t  # local t and not account for scr refresh
            mask3_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask3_11, 'tStartRefresh')  # time at next scr refresh
            mask3_11.setAutoDraw(True)
        if mask3_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask3_11.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask3_11.tStop = t  # not accounting for scr refresh
                mask3_11.frameNStop = frameN  # exact frame index
                mask3_11.setAutoDraw(False)
        
        # *mask4_11* updates
        if mask4_11.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask4_11.frameNStart = frameN  # exact frame index
            mask4_11.tStart = t  # local t and not account for scr refresh
            mask4_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask4_11, 'tStartRefresh')  # time at next scr refresh
            mask4_11.setAutoDraw(True)
        if mask4_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask4_11.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask4_11.tStop = t  # not accounting for scr refresh
                mask4_11.frameNStop = frameN  # exact frame index
                mask4_11.setAutoDraw(False)
        
        # *Change_grating_11* updates
        if Change_grating_11.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            Change_grating_11.frameNStart = frameN  # exact frame index
            Change_grating_11.tStart = t  # local t and not account for scr refresh
            Change_grating_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Change_grating_11, 'tStartRefresh')  # time at next scr refresh
            Change_grating_11.setAutoDraw(True)
        if Change_grating_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Change_grating_11.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                Change_grating_11.tStop = t  # not accounting for scr refresh
                Change_grating_11.frameNStop = frameN  # exact frame index
                Change_grating_11.setAutoDraw(False)
        
        # *Trial_Resp_11* updates
        waitOnFlip = False
        if Trial_Resp_11.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            Trial_Resp_11.frameNStart = frameN  # exact frame index
            Trial_Resp_11.tStart = t  # local t and not account for scr refresh
            Trial_Resp_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_Resp_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_Resp_11.started')
            Trial_Resp_11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Trial_Resp_11.clock.reset)  # t=0 on next screen flip
        if Trial_Resp_11.status == STARTED and not waitOnFlip:
            theseKeys = Trial_Resp_11.getKeys(keyList=['left','right'], waitRelease=False)
            _Trial_Resp_11_allKeys.extend(theseKeys)
            if len(_Trial_Resp_11_allKeys):
                Trial_Resp_11.keys = _Trial_Resp_11_allKeys[0].name  # just the first key pressed
                Trial_Resp_11.rt = _Trial_Resp_11_allKeys[0].rt
                # was this correct?
                if (Trial_Resp_11.keys == str(CorrectAns)) or (Trial_Resp_11.keys == CorrectAns):
                    Trial_Resp_11.corr = 1
                else:
                    Trial_Resp_11.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *ISI_11* period
        if ISI_11.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_11.frameNStart = frameN  # exact frame index
            ISI_11.tStart = t  # local t and not account for scr refresh
            ISI_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_11, 'tStartRefresh')  # time at next scr refresh
            ISI_11.start(0.5)
        elif ISI_11.status == STARTED:  # one frame should pass before updating params and completing
            ISI_11.complete()  # finish the static period
            ISI_11.tStop = ISI_11.tStart + 0.5  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial9Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial9" ---
    for thisComponent in Trial9Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from Set_CW_CCW_11
    
            
    # check responses
    if Trial_Resp_11.keys in ['', [], None]:  # No response was made
        Trial_Resp_11.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Trial_Resp_11.corr = 1;  # correct non-response
        else:
           Trial_Resp_11.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_9 (MultiStairHandler)
    trials_9.addResponse(Trial_Resp_11.corr, level)
    trials_9.addOtherData('Trial_Resp_11.rt', Trial_Resp_11.rt)
    # the Routine "Trial9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# all staircases completed


# set up handler to look after randomisation of trials etc
conditions = data.importConditions('Stairs.xlsx')
Adapt_Stair = data.MultiStairHandler(stairType='simple', name='Adapt_Stair',
    nTrials=1.0,
    conditions=conditions,
    method='random',
    originPath=-1)
thisExp.addLoop(Adapt_Stair)  # add the loop to the experiment
# initialise values for first condition
level = Adapt_Stair._nextIntensity  # initialise some vals
condition = Adapt_Stair.currentStaircase.condition

for level, condition in Adapt_Stair:
    currentLoop = Adapt_Stair
    # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
    for paramName in condition:
        exec(paramName + '= condition[paramName]')
    
    # --- Prepare to start Routine "Trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Set_CW_CCW
    myCount11 = myCount11 + 1
    if myCount11 == 10:
        Adapt_Stair.finished = True
    if random() > 0.5:
        Ori_Grat=Base_Ori+level #positive so CW
        CorrectAns='right'
        
    else:
        Ori_Grat= Base_Ori - level #negative do ccw
        CorrectAns='left'
    # Run 'Begin Routine' code from Set_Mask_Orientations
    listnames=[]
    for x in range(1,5):
        listnames.append("maskorient" +str(x))
        print(listnames)
        
    for y in range(0,4):
        exec("%s=%d" % (listnames[y], random()*360))
        
    
    base_grating.setOri(Base_Ori)
    mask1.setOri(maskorient1)
    mask2.setOri(maskorient2)
    mask3.setOri(maskorient3)
    mask4.setOri(maskorient4)
    Change_grating.setOri(Ori_Grat)
    Trial_Resp.keys = []
    Trial_Resp.rt = []
    _Trial_Resp_allKeys = []
    # keep track of which components have finished
    TrialComponents = [ISI, base_grating, mask1, mask2, mask3, mask4, Change_grating, Trial_Resp]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *base_grating* updates
        if base_grating.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            base_grating.frameNStart = frameN  # exact frame index
            base_grating.tStart = t  # local t and not account for scr refresh
            base_grating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(base_grating, 'tStartRefresh')  # time at next scr refresh
            base_grating.setAutoDraw(True)
        if base_grating.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > base_grating.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                base_grating.tStop = t  # not accounting for scr refresh
                base_grating.frameNStop = frameN  # exact frame index
                base_grating.setAutoDraw(False)
        
        # *mask1* updates
        if mask1.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask1.frameNStart = frameN  # exact frame index
            mask1.tStart = t  # local t and not account for scr refresh
            mask1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask1, 'tStartRefresh')  # time at next scr refresh
            mask1.setAutoDraw(True)
        if mask1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask1.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask1.tStop = t  # not accounting for scr refresh
                mask1.frameNStop = frameN  # exact frame index
                mask1.setAutoDraw(False)
        
        # *mask2* updates
        if mask2.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask2.frameNStart = frameN  # exact frame index
            mask2.tStart = t  # local t and not account for scr refresh
            mask2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask2, 'tStartRefresh')  # time at next scr refresh
            mask2.setAutoDraw(True)
        if mask2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask2.tStop = t  # not accounting for scr refresh
                mask2.frameNStop = frameN  # exact frame index
                mask2.setAutoDraw(False)
        
        # *mask3* updates
        if mask3.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask3.frameNStart = frameN  # exact frame index
            mask3.tStart = t  # local t and not account for scr refresh
            mask3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask3, 'tStartRefresh')  # time at next scr refresh
            mask3.setAutoDraw(True)
        if mask3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask3.tStop = t  # not accounting for scr refresh
                mask3.frameNStop = frameN  # exact frame index
                mask3.setAutoDraw(False)
        
        # *mask4* updates
        if mask4.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask4.frameNStart = frameN  # exact frame index
            mask4.tStart = t  # local t and not account for scr refresh
            mask4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask4, 'tStartRefresh')  # time at next scr refresh
            mask4.setAutoDraw(True)
        if mask4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask4.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask4.tStop = t  # not accounting for scr refresh
                mask4.frameNStop = frameN  # exact frame index
                mask4.setAutoDraw(False)
        
        # *Change_grating* updates
        if Change_grating.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            Change_grating.frameNStart = frameN  # exact frame index
            Change_grating.tStart = t  # local t and not account for scr refresh
            Change_grating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Change_grating, 'tStartRefresh')  # time at next scr refresh
            Change_grating.setAutoDraw(True)
        if Change_grating.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Change_grating.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                Change_grating.tStop = t  # not accounting for scr refresh
                Change_grating.frameNStop = frameN  # exact frame index
                Change_grating.setAutoDraw(False)
        
        # *Trial_Resp* updates
        waitOnFlip = False
        if Trial_Resp.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            Trial_Resp.frameNStart = frameN  # exact frame index
            Trial_Resp.tStart = t  # local t and not account for scr refresh
            Trial_Resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_Resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_Resp.started')
            Trial_Resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Trial_Resp.clock.reset)  # t=0 on next screen flip
        if Trial_Resp.status == STARTED and not waitOnFlip:
            theseKeys = Trial_Resp.getKeys(keyList=['left','right'], waitRelease=False)
            _Trial_Resp_allKeys.extend(theseKeys)
            if len(_Trial_Resp_allKeys):
                Trial_Resp.keys = _Trial_Resp_allKeys[0].name  # just the first key pressed
                Trial_Resp.rt = _Trial_Resp_allKeys[0].rt
                # was this correct?
                if (Trial_Resp.keys == str(CorrectAns)) or (Trial_Resp.keys == CorrectAns):
                    Trial_Resp.corr = 1
                else:
                    Trial_Resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *ISI* period
        if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI.frameNStart = frameN  # exact frame index
            ISI.tStart = t  # local t and not account for scr refresh
            ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            ISI.start(0.5)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
            ISI.tStop = ISI.tStart + 0.5  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial" ---
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Trial_Resp.keys in ['', [], None]:  # No response was made
        Trial_Resp.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Trial_Resp.corr = 1;  # correct non-response
        else:
           Trial_Resp.corr = 0;  # failed to respond (incorrectly)
    # store data for Adapt_Stair (MultiStairHandler)
    Adapt_Stair.addResponse(Trial_Resp.corr, level)
    Adapt_Stair.addOtherData('Trial_Resp.rt', Trial_Resp.rt)
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# all staircases completed


# set up handler to look after randomisation of trials etc
conditions = data.importConditions('Stairs.xlsx')
trials_10 = data.MultiStairHandler(stairType='simple', name='trials_10',
    nTrials=1.0,
    conditions=conditions,
    method='random',
    originPath=-1)
thisExp.addLoop(trials_10)  # add the loop to the experiment
# initialise values for first condition
level = trials_10._nextIntensity  # initialise some vals
condition = trials_10.currentStaircase.condition

for level, condition in trials_10:
    currentLoop = trials_10
    # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
    for paramName in condition:
        exec(paramName + '= condition[paramName]')
    
    # --- Prepare to start Routine "Trial_11" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Set_CW_CCW_3
    myCount12 = myCount12 + 1
    if myCount12 == 10:
        trials_10.finished = True
    if random() > 0.5:
        Ori_Grat=Base_Ori+level #positive so CW
        CorrectAns='right'
        
    else:
        Ori_Grat= Base_Ori - level #negative do ccw
        CorrectAns='left'
    # Run 'Begin Routine' code from Set_Mask_Orientations_3
    listnames=[]
    for x in range(1,5):
        listnames.append("maskorient" +str(x))
        print(listnames)
        
    for y in range(0,4):
        exec("%s=%d" % (listnames[y], random()*360))
        
    
    base_grating_3.setOri(Base_Ori)
    mask1_3.setOri(maskorient1)
    mask2_3.setOri(maskorient2)
    mask3_3.setOri(maskorient3)
    mask4_3.setOri(maskorient4)
    Change_grating_3.setOri(Ori_Grat)
    Trial_Resp_3.keys = []
    Trial_Resp_3.rt = []
    _Trial_Resp_3_allKeys = []
    # keep track of which components have finished
    Trial_11Components = [ISI_3, base_grating_3, mask1_3, mask2_3, mask3_3, mask4_3, Change_grating_3, Trial_Resp_3]
    for thisComponent in Trial_11Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Trial_11" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *base_grating_3* updates
        if base_grating_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            base_grating_3.frameNStart = frameN  # exact frame index
            base_grating_3.tStart = t  # local t and not account for scr refresh
            base_grating_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(base_grating_3, 'tStartRefresh')  # time at next scr refresh
            base_grating_3.setAutoDraw(True)
        if base_grating_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > base_grating_3.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                base_grating_3.tStop = t  # not accounting for scr refresh
                base_grating_3.frameNStop = frameN  # exact frame index
                base_grating_3.setAutoDraw(False)
        
        # *mask1_3* updates
        if mask1_3.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask1_3.frameNStart = frameN  # exact frame index
            mask1_3.tStart = t  # local t and not account for scr refresh
            mask1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask1_3, 'tStartRefresh')  # time at next scr refresh
            mask1_3.setAutoDraw(True)
        if mask1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask1_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask1_3.tStop = t  # not accounting for scr refresh
                mask1_3.frameNStop = frameN  # exact frame index
                mask1_3.setAutoDraw(False)
        
        # *mask2_3* updates
        if mask2_3.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask2_3.frameNStart = frameN  # exact frame index
            mask2_3.tStart = t  # local t and not account for scr refresh
            mask2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask2_3, 'tStartRefresh')  # time at next scr refresh
            mask2_3.setAutoDraw(True)
        if mask2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask2_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask2_3.tStop = t  # not accounting for scr refresh
                mask2_3.frameNStop = frameN  # exact frame index
                mask2_3.setAutoDraw(False)
        
        # *mask3_3* updates
        if mask3_3.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask3_3.frameNStart = frameN  # exact frame index
            mask3_3.tStart = t  # local t and not account for scr refresh
            mask3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask3_3, 'tStartRefresh')  # time at next scr refresh
            mask3_3.setAutoDraw(True)
        if mask3_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask3_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask3_3.tStop = t  # not accounting for scr refresh
                mask3_3.frameNStop = frameN  # exact frame index
                mask3_3.setAutoDraw(False)
        
        # *mask4_3* updates
        if mask4_3.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask4_3.frameNStart = frameN  # exact frame index
            mask4_3.tStart = t  # local t and not account for scr refresh
            mask4_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask4_3, 'tStartRefresh')  # time at next scr refresh
            mask4_3.setAutoDraw(True)
        if mask4_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask4_3.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask4_3.tStop = t  # not accounting for scr refresh
                mask4_3.frameNStop = frameN  # exact frame index
                mask4_3.setAutoDraw(False)
        
        # *Change_grating_3* updates
        if Change_grating_3.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            Change_grating_3.frameNStart = frameN  # exact frame index
            Change_grating_3.tStart = t  # local t and not account for scr refresh
            Change_grating_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Change_grating_3, 'tStartRefresh')  # time at next scr refresh
            Change_grating_3.setAutoDraw(True)
        if Change_grating_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Change_grating_3.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                Change_grating_3.tStop = t  # not accounting for scr refresh
                Change_grating_3.frameNStop = frameN  # exact frame index
                Change_grating_3.setAutoDraw(False)
        
        # *Trial_Resp_3* updates
        waitOnFlip = False
        if Trial_Resp_3.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            Trial_Resp_3.frameNStart = frameN  # exact frame index
            Trial_Resp_3.tStart = t  # local t and not account for scr refresh
            Trial_Resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_Resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_Resp_3.started')
            Trial_Resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Trial_Resp_3.clock.reset)  # t=0 on next screen flip
        if Trial_Resp_3.status == STARTED and not waitOnFlip:
            theseKeys = Trial_Resp_3.getKeys(keyList=['left','right'], waitRelease=False)
            _Trial_Resp_3_allKeys.extend(theseKeys)
            if len(_Trial_Resp_3_allKeys):
                Trial_Resp_3.keys = _Trial_Resp_3_allKeys[0].name  # just the first key pressed
                Trial_Resp_3.rt = _Trial_Resp_3_allKeys[0].rt
                # was this correct?
                if (Trial_Resp_3.keys == str(CorrectAns)) or (Trial_Resp_3.keys == CorrectAns):
                    Trial_Resp_3.corr = 1
                else:
                    Trial_Resp_3.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *ISI_3* period
        if ISI_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_3.frameNStart = frameN  # exact frame index
            ISI_3.tStart = t  # local t and not account for scr refresh
            ISI_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_3, 'tStartRefresh')  # time at next scr refresh
            ISI_3.start(0.5)
        elif ISI_3.status == STARTED:  # one frame should pass before updating params and completing
            ISI_3.complete()  # finish the static period
            ISI_3.tStop = ISI_3.tStart + 0.5  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial_11Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial_11" ---
    for thisComponent in Trial_11Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Trial_Resp_3.keys in ['', [], None]:  # No response was made
        Trial_Resp_3.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Trial_Resp_3.corr = 1;  # correct non-response
        else:
           Trial_Resp_3.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_10 (MultiStairHandler)
    trials_10.addResponse(Trial_Resp_3.corr, level)
    trials_10.addOtherData('Trial_Resp_3.rt', Trial_Resp_3.rt)
    # the Routine "Trial_11" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# all staircases completed


# set up handler to look after randomisation of trials etc
conditions = data.importConditions('Stairs.xlsx')
trials_11 = data.MultiStairHandler(stairType='simple', name='trials_11',
    nTrials=1.0,
    conditions=conditions,
    method='random',
    originPath=-1)
thisExp.addLoop(trials_11)  # add the loop to the experiment
# initialise values for first condition
level = trials_11._nextIntensity  # initialise some vals
condition = trials_11.currentStaircase.condition

for level, condition in trials_11:
    currentLoop = trials_11
    # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
    for paramName in condition:
        exec(paramName + '= condition[paramName]')
    
    # --- Prepare to start Routine "Trial12" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Set_CW_CCW_12
    myCount13 = myCount13 + 1
    if myCount13 == 10:
        trials_11.finished = True
    if random() > 0.5:
        Ori_Grat=Base_Ori+level #positive so CW
        CorrectAns='right'
        
    else:
        Ori_Grat= Base_Ori - level #negative do ccw
        CorrectAns='left'
    # Run 'Begin Routine' code from Set_Mask_Orientations_12
    listnames=[]
    for x in range(1,5):
        listnames.append("maskorient" +str(x))
        print(listnames)
        
    for y in range(0,4):
        exec("%s=%d" % (listnames[y], random()*360))
        
    
    base_grating_12.setOri(Base_Ori)
    mask1_12.setOri(maskorient1)
    mask2_12.setOri(maskorient2)
    mask3_12.setOri(maskorient3)
    mask4_12.setOri(maskorient4)
    Change_grating_12.setOri(Ori_Grat)
    Trial_Resp_12.keys = []
    Trial_Resp_12.rt = []
    _Trial_Resp_12_allKeys = []
    # keep track of which components have finished
    Trial12Components = [ISI_12, base_grating_12, mask1_12, mask2_12, mask3_12, mask4_12, Change_grating_12, Trial_Resp_12]
    for thisComponent in Trial12Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Trial12" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *base_grating_12* updates
        if base_grating_12.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            base_grating_12.frameNStart = frameN  # exact frame index
            base_grating_12.tStart = t  # local t and not account for scr refresh
            base_grating_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(base_grating_12, 'tStartRefresh')  # time at next scr refresh
            base_grating_12.setAutoDraw(True)
        if base_grating_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > base_grating_12.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                base_grating_12.tStop = t  # not accounting for scr refresh
                base_grating_12.frameNStop = frameN  # exact frame index
                base_grating_12.setAutoDraw(False)
        
        # *mask1_12* updates
        if mask1_12.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask1_12.frameNStart = frameN  # exact frame index
            mask1_12.tStart = t  # local t and not account for scr refresh
            mask1_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask1_12, 'tStartRefresh')  # time at next scr refresh
            mask1_12.setAutoDraw(True)
        if mask1_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask1_12.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask1_12.tStop = t  # not accounting for scr refresh
                mask1_12.frameNStop = frameN  # exact frame index
                mask1_12.setAutoDraw(False)
        
        # *mask2_12* updates
        if mask2_12.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask2_12.frameNStart = frameN  # exact frame index
            mask2_12.tStart = t  # local t and not account for scr refresh
            mask2_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask2_12, 'tStartRefresh')  # time at next scr refresh
            mask2_12.setAutoDraw(True)
        if mask2_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask2_12.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask2_12.tStop = t  # not accounting for scr refresh
                mask2_12.frameNStop = frameN  # exact frame index
                mask2_12.setAutoDraw(False)
        
        # *mask3_12* updates
        if mask3_12.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask3_12.frameNStart = frameN  # exact frame index
            mask3_12.tStart = t  # local t and not account for scr refresh
            mask3_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask3_12, 'tStartRefresh')  # time at next scr refresh
            mask3_12.setAutoDraw(True)
        if mask3_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask3_12.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask3_12.tStop = t  # not accounting for scr refresh
                mask3_12.frameNStop = frameN  # exact frame index
                mask3_12.setAutoDraw(False)
        
        # *mask4_12* updates
        if mask4_12.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            mask4_12.frameNStart = frameN  # exact frame index
            mask4_12.tStart = t  # local t and not account for scr refresh
            mask4_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask4_12, 'tStartRefresh')  # time at next scr refresh
            mask4_12.setAutoDraw(True)
        if mask4_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mask4_12.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                mask4_12.tStop = t  # not accounting for scr refresh
                mask4_12.frameNStop = frameN  # exact frame index
                mask4_12.setAutoDraw(False)
        
        # *Change_grating_12* updates
        if Change_grating_12.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            Change_grating_12.frameNStart = frameN  # exact frame index
            Change_grating_12.tStart = t  # local t and not account for scr refresh
            Change_grating_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Change_grating_12, 'tStartRefresh')  # time at next scr refresh
            Change_grating_12.setAutoDraw(True)
        if Change_grating_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Change_grating_12.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                Change_grating_12.tStop = t  # not accounting for scr refresh
                Change_grating_12.frameNStop = frameN  # exact frame index
                Change_grating_12.setAutoDraw(False)
        
        # *Trial_Resp_12* updates
        waitOnFlip = False
        if Trial_Resp_12.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            Trial_Resp_12.frameNStart = frameN  # exact frame index
            Trial_Resp_12.tStart = t  # local t and not account for scr refresh
            Trial_Resp_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_Resp_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_Resp_12.started')
            Trial_Resp_12.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Trial_Resp_12.clock.reset)  # t=0 on next screen flip
        if Trial_Resp_12.status == STARTED and not waitOnFlip:
            theseKeys = Trial_Resp_12.getKeys(keyList=['left','right'], waitRelease=False)
            _Trial_Resp_12_allKeys.extend(theseKeys)
            if len(_Trial_Resp_12_allKeys):
                Trial_Resp_12.keys = _Trial_Resp_12_allKeys[0].name  # just the first key pressed
                Trial_Resp_12.rt = _Trial_Resp_12_allKeys[0].rt
                # was this correct?
                if (Trial_Resp_12.keys == str(CorrectAns)) or (Trial_Resp_12.keys == CorrectAns):
                    Trial_Resp_12.corr = 1
                else:
                    Trial_Resp_12.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *ISI_12* period
        if ISI_12.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI_12.frameNStart = frameN  # exact frame index
            ISI_12.tStart = t  # local t and not account for scr refresh
            ISI_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI_12, 'tStartRefresh')  # time at next scr refresh
            ISI_12.start(0.5)
        elif ISI_12.status == STARTED:  # one frame should pass before updating params and completing
            ISI_12.complete()  # finish the static period
            ISI_12.tStop = ISI_12.tStart + 0.5  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial12Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial12" ---
    for thisComponent in Trial12Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Trial_Resp_12.keys in ['', [], None]:  # No response was made
        Trial_Resp_12.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           Trial_Resp_12.corr = 1;  # correct non-response
        else:
           Trial_Resp_12.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_11 (MultiStairHandler)
    trials_11.addResponse(Trial_Resp_12.corr, level)
    trials_11.addOtherData('Trial_Resp_12.rt', Trial_Resp_12.rt)
    # the Routine "Trial12" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# all staircases completed


# --- Prepare to start Routine "Thank_You" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
Thank_YouComponents = [Thank_Yo]
for thisComponent in Thank_YouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Thank_You" ---
while continueRoutine and routineTimer.getTime() < 6.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Thank_Yo* updates
    if Thank_Yo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Thank_Yo.frameNStart = frameN  # exact frame index
        Thank_Yo.tStart = t  # local t and not account for scr refresh
        Thank_Yo.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Thank_Yo, 'tStartRefresh')  # time at next scr refresh
        Thank_Yo.setAutoDraw(True)
    if Thank_Yo.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Thank_Yo.tStartRefresh + 6.0-frameTolerance:
            # keep track of stop time/frame for later
            Thank_Yo.tStop = t  # not accounting for scr refresh
            Thank_Yo.frameNStop = frameN  # exact frame index
            Thank_Yo.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Thank_YouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Thank_You" ---
for thisComponent in Thank_YouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-6.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
