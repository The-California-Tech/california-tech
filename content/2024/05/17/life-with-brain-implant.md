---
title: "Life with a Brain Implant: Interview with clinical trial subject James Johnson"
authors:
  - Sanvi Pal
date: 2024-05-17 08:00:00 -0700
categories:
  - Science & Tech
tags:
  - 'Vol. CXXVII, Issue 14'
weight: 0
show_thumbnail: false
thumbnail: /default4.jpg
images:
  - /default4.jpg
sidebar: right
toc: false
widgets:
  - write-for-the-tech
  - editorial
  - taglist
  - categories
  - recent
summary: >-
    In the field of Neurotechnology, there is a lot of work being done to use brain machine interfaces to help people with motor disabilities regain lost abilities. When reading Professor Andersen's papers as a high schooler, I remember thinking: this is the kind of research that can help a lot of people.
---

When I applied to Caltech, I applied because I was in awe of Professor Richard Andersen and the work he and his graduate students have done with brain machine interfaces (BMI) — devices that are able to both pick up neural activity and transmit signals to the brain. 

# The Science Picture

BMI systems can be open-loop or closed-loop. Open-loop means that there is a pre-programmed system output regardless of what the user is thinking. Closed-loop means that the subject is now integrated in the loop and has control over system output. There are two kinds of BMIs, "write-in" and "read-out". A "write-in" BMI transfers electrical pulses to send signals to parts of the brain. An example of a "write-in" BMI is Deep-Brain Stimulation which is a treatment option for people with Parkinson's Disease where electrodes are used to stimulate motion related areas of the brain to decrease tremors. A "read-out" BMI records brain activity. These "read-out" BMIs can be invasive (require neurosurgery and/or implantation) or non-invasive (devices reside on the skin of the scalp or skin near relevant muscles). Examples of recording devices used in "read-out" brain machine interfaces are EMG (Electromyography), ECoG (Electrocorticography), EEG (Electroencephalography), fMRI (Functional Magnetic Resonance Imaging), fUS (functional Ultrasound), and intracortical arrays. EMG records electrical activity from skeletal muscles and EEG records electrical activity from the scalp. ECoG records electrical activity from the brain surface (cortex). fMRI uses magnetic fields to measure changes in blood flow and oxygen levels and this is used to identify the tasks certain brain regions are responsible for (can also be used to direct location of implants). fUS uses ultrasound to record changes in blood volume. Intracortical arrays have tiny microelectrodes that pick up electrophysiological signals from neurons (signals caused by action potentials).

The Andersen Lab is involved in invasive brain machine interface research related to decoding electrical signals from the brain. Decoding involves taking in raw brain signals and using machine learning and mathematical algorithms to map patterns in neural activity to signal(s) representing the subject's goal. 

The Andersen Lab uses linear decoders. Their continuous decoder employs linear regression which maps certain channels of activity to motion. For example, their subject will initially be in an open-loop run of the task, during which they follow along with movements made by a computer controlled cursor as their neural activity is recorded. To give the subject control in closed-loop, the data in this run is then used for the initial training of the decoder and gives information about channels of activity/what neurons are predictive of x direction and what neurons are predictive of y direction. The outcome of this regression are weights to neurons based on the neurons' involvement in the motion. While some actions like controlling a cursor on a computer are more continuous in nature, other actions like clicking the mouse, can be considered discrete. For this case, the Andersen lab also has a discrete decoder which does linear discriminant analysis classification to make movement choices before the movement. A critical step in training both continuous and discrete decoders is choosing what features of the neural activity—an electrical signal—are actually predictive of the participant's intentions. In the beginning of the study, they used threshold crossings (for each channel the number of times the voltage crosses a threshold) to train the linear decoder, but now they use a neural network for feature extraction. The neural network, called FENET, identifies relevant neural activity based on a broadband signal which includes both multiunit activity and spikes. This advanced feature extraction is needed because over time the signal degrades. When the patient first gets hooked up, brain control is fantastic using traditional methods (i.e. threshold crossings). Over time it takes more effort and the implant shifts. FENET (developed in collaboration with the Emami group) is able to fill in the blanks on the signals. It restores the level of control to what it was at the start of the study. 

# The Human Picture

In the field of Neurotechnology, there is a lot of work being done to use brain machine interfaces to help people with motor disabilities regain lost abilities. When reading Professor Andersen's papers as a high schooler, I remember thinking: this is the kind of research that can help a lot of people. That's why, in my second year of being an undergrad here, I jumped on the opportunity of taking CNS 256 Brain Machine Interfaces with Professor Richard Andersen. His graduate student Kelly Kadlec (Neurobiology, G6) has had a huge role in structuring this class as well, and I greatly appreciate her work. 

In one class, we all got the opportunity to have an inspirational conversation with James Johnson, a clinical trial patient at the Andersen Lab. James is tetraplegic; he can't move anything below his chest, can't close his hand, and has a fractured but not severed spine.

James has been a member of this study for 6 years. He has received two implants of Blackrock's Utah Array (an intracortical array), one in the left posterior parietal cortex (region in the brain responsible for planning motor decisions) and one in the left motor cortex (region responsible for sending motor commands to the spinal cord). The Utah Array is a 4 mm x 4mm 128 microelectrode array made by Blackrock that can record and stimulate neurons for decoding applications. James works with the Andersen Lab 3-4 days a week and participates in 2-3 hour sessions a day. The Andersen lab uses the sessions to collect data and tries new interfaces for James to test. In these sessions, James does various tasks like play video games or move a cursor by thinking about the action. In this setup, he is able to "will things to move" as he is able to cause movement on the screen from his thoughts.

It was truly inspiring to meet with James and hear first hand experiences about the surprising scope of abilities unlocked from neural decoding. 


# Interview with James Johnson


## Q1: Why did you join the study?
A: Before the injury, I was both a respiratory therapist and a registered nurse who'd worked in many hospitals throughout California. Working in healthcare gave me the opportunity to give back and help people. When the accident occurred, I was utterly devastated to discover I had lost movement. Naturally, I wasn't hesitant to participate in the program because I felt it was an opportunity to give back again. 

## Q2: Did you have any reservations? What was your perspective going into the surgery process? What parts of it were scary and what parts were exciting?
A: I worked with many individuals that had brain issues. I was familiar with where they wanted to place the electrodes/chips so I wasn't scared about that. I was most concerned about what I look like afterwards. I wasn't really concerned/afraid of the procedure itself.

## Q3: What was the surgery process like?
A: I wanted to see the surgery so I asked someone to record it. I found it cool to see my own brain. They opened the whole scalp and skull to put in the electrodes. I also was surprised with how long it took. It took 8 hours.

## Q4: What were your initial thoughts?
A: I thought I felt like a Jedi. I was willing things to move. You have that sensation that you are special. Over the past five years, I have been pushing my abilities to its limits. I love gaming and we are playing chess and call of duty. I also love art and am able to make things with a workshop at home through photoshopping. When we first got started, it was very fatiguing to will something to happen. It's like going to the gym for the first time and lifting weights. Over time you build more stamina and muscle. Weight lifting becomes easier and you advance to heavier weights. That is how it feels to will something to move on the screen. I took time to adapt to tasks that were asked. I really needed to harness energy to focus on the task at hand and over time the tasks got harder. 

## Q5: Describe the strategies where you are attempting to move in the way you move and how that differs?
A: First, I was told to imagine my thumbs following the target. This was easy for me as I was able to immediately imagine moving the joystick in a game controller with my thumb. The control I had was dependent on muscle memory. So it was simple to imagine moving my thumb. After three months, I was able to use thoughts instead of actively imagining my hand doing something. This requires a lot of concentration.

## Q6: Describe different types of willing movement (controlling with the mind vs body parts)?
A: One experiment I did was speeding up the cursor. First, I thought about moving the cursor with my hands. Eventually I was asked: can you move the cursor with your feet or knees? When I try to use my foot, it takes a lot of effort. Maybe it's the distance the neural pathways need to follow but I felt more fatigued. Over time, I built stamina.

## Q7: How are sessions optimized?
A: Different signals light up when decoding. When I think of moving the cursor, different neurons send signals that the decoder can use. There are different regions of neurons that send signals based on what I am thinking about to move the cursor. For example, there are different channels that get tuned based on hand and foot movement.

## Q8: Describe the session logistics.
A: I am able to go on for longer sessions now. Sessions are 2-3 hours. My mind does wander. This is obvious as the cursor on the screen pulls away. If I am having one of those days when I am struggling against the decoder, it is very fatiguing. I had built up stamina but there are those days when the decoder doesn't cooperate. I take 3-4 minute breaks to sort of reset before continuing the session.

## Q9: What happens after some sort of holiday?
A: My fatigue and effort is the same as the last time I recorded. It is like riding a bike and running off. When I play a video game, the excitement precedes the fatigue. 

## Q10: Are there any tasks that you have done without viewing any screen?
A: Last week, postdoc Jorge Gamez was thinking we are using eye tracking. So in front of him, I tried to move the cursor without moving my gaze. It was very successful. I successfully moved the cursor and landed on targets. It is like typing or texting without looking at the phone. 

## Q11: What kind of sensations/motor ability does doing digital art require?
A: We need to train the decoder to have multiple digits [degrees of freedom for movement]. We need to click and hold to draw and fade. The decoder can be trained for the thumb or  the whole hand. My hand is still and I imagine moving my hand. 

## Q12: Would you consider replacement (replacing limbs with prosthetics)?
A: Sometimes I work with manufacturers of Blackrock. We have below-the-elbow amputees. They gave one amputee a prosthetic arm. There is a chip that picks up muscle activity of the arm above amputation level. He can take off the arm and still control it. He can move the hand while it is detached. I want to see some bridge between different levels of spinal cord injury. So above the C4, make a device that connects from C3 to C6 so that the signal carries across the bridge. Bridging this gap between intact parts of the spinal cord can allow signal transmission and restore communication between the brain and body parts that couldn't move due to injury.

## Q13: What should people who want to work with humans with brain implants know?
A: It is good to allow the participants to give input. This makes the subject feel that their input is valid and allows for a more cohesive relationship with the people you work with in projects. For example, I am able to develop tasks related to what I like to do [like video games and digital art].

## Q14: What kind of things do you expect in the future? Do you have a vision?
A: I want to see brain-computer interfaces combined with functional electrical stimulation (FES) so that we can control robotic appendages or an exoskeleton. We need an exoskeleton to allow tetraplegic people to close fingers and grab things. I want to be able to send signals to external devices and will move according to my thoughts. FES is functional electrical stimulation and can use current to cause muscle stimulation that elicits movement. For people that are not amputees, we might be able to develop an exoskeleton to perform motor functions. We can be able to map the brain enough to have people that are paralyzed or partially paralyzed control movement.

*Special thank you to Professor Andersen, Kelly Kadlec, and James Johnson for editing and helping me write this.*