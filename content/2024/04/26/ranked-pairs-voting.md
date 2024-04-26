---
title: 'On Ranked Pairs Voting'
authors:
  - Alejandro Lopez
  - Maya Mutic
date: 2024-04-26 08:00:00 -0700
categories:
  - Letter to the Editor
tags:
  - 'Vol. CXXVII, Issue 13'
weight: 0
show_thumbnail: false
thumbnail: /default5.jpg
images:
  - /default5.jpg
sidebar: right
toc: false
widgets:
  - write-for-the-tech
  - editorial
  - taglist
  - categories
  - recent
summary: >-
    My intention is to address all current undergrads so they might appreciate Ranked Pairs as a voting system.
---

Dear Editors,

A few months ago I learned that in the course of conducting its elections, Ricketts Hovse was unsure which exact voting method to use. At first, I and a few other alumni were shocked and disappointed; only a few years ago, a number of then students including myself had worked to switch Ricketts, several other houses, and ASCIT over to what we considered the most ideal voting system for us, the "Ranked Pairs" or "Tideman" method. But taking a step back, it makes sense that nuances might have been lost over time, especially across the pandemic. At the time those changes occurred, because of widespread discussion, voting systems were almost as much on the minds of students as the game *Pokemon Go* (perhaps hyperbole). Additionally, Professor Ordeshook's version of PS 12 covered voting systems extensively, and I have also learned he no longer teaches that course. As an aside, I apologize Ricketts never kept of permanent written record of this change, but it occurred before I was Ricketts secretary. My intention though now is not to dwell on the shortsightedness of Ricketts at the time, but to address all current undergrads so they might appreciate Ranked Pairs as a voting system.

**What is the Ideal Voting System?** 

There is no ideal voting system, according to math done by people a lot smarter than me. More precisely, of the many criteria that can be imposed to determine what a "good" voting system is, no single system can satisfy all of them.

Many students are hopefully familiar with major issues with certain common voting systems however. The "first-past-the-post" or "plurality" system allows candidates to win without a majority of votes, and is very vulnerable to spoiler effects and strategic voting and becomes especially unideal for elections with many candidates. No group I'm aware of at Caltech uses plurality voting, but much of the United States uses it for many elections.

An improvement over this system is the "two-round" system which takes the top two candidates and runs a new run-off election to decide the winner. This ensures the winner wins with a majority. This system is still used by Fleming, and a similar system is still used by Page. Out in the real world, California uses two-round system extensively.

The two-round system is only a slight improvement over plurality voting and still suffers from several issues. Notably, focusing on the top two candidates adds an element of arbitrariness to the system, especially since voters can only express a single preference. Additionally, the system requires the extra time to run run-offs in some cases. A natural improvement is to instead have voters vote only once with ranked preferences, and then conduct a series of "instant" runoffs, where candidates are eliminated one by one during counting by whoever has the fewest votes, and votes are redistributed to the next candidate each voter prefers. This method is known as instant runoff voting (IRV) and it's the most common form of ranked choice voting. It's currently used for single-winner elections in Lloyd and Avery and is used in San Francisco and a few other state and local government elections across the US. Ranked pairs was mistaken for IRV in Ricketts this year precisely because it is so common.

**A brief history of voting systems at Caltech** 

Voting at Caltech has followed the evolution in thinking as I just described; for most of the 20th century (as far as I've found) ASCIT and the houses conducted elections using a simple two-round system, with separate runoffs occurring in the event one candidate didn't initially reach a majority. At some point in the late 1980s or early 1990s, ASCIT voted to switch to IRV. Most of the Houses (except Page and Fleming) switched to that system at some point as well. Most recently in the late 2010s, some students saw issue with IRV. IRV is still dependent on eliminating candidates, which can arbitrarily influence results. The 2016 Ricketts Secretary special election resulted in a bizarre occurrence where changing a single vote would have altered the winner merely because of the elimination order. IRV also fails one criterion students deemed important, the Condorcet criterion, which says that the winner should beat any other candidate in a head-to-head matchup. Voting systems that meet this criterion are known collectively as Condorcet methods, and students settled one of them, Ranked Pairs. Ricketts, Dabney, Blacker, and Venerable (then Ruddock) each voted to switch to Ranked Pairs around the same time. ASCIT voted to switch in November 2017, with over 80% of students campus-wide supporting the amendment.

**How Ranked Pairs Works** 

The best way to think of Condorcet election methods is as a round-robin contest; each candidate/ticket is compared to each other. In each pair (A,B) , the winner is simply the candidate whom more voters rank higher. If a single candidate is found that beats all the candidates, that candidate is called the Condorcet winner. Condorcet methods always elect the Condorcet winner where one exists; they differ in how they determine the winner in cases where there is no Condorcet winner, wherein a "cycle" exists. A cycle is a scenario like the game rock-paper-scissors where A beats B, B beats C, and C beats A. Ranked pairs avoids cycles by "locking in" pairs sequentially by "strength," giving preference to pairs where one candidate beat the other candidate by a greater margin (hence the name, "Ranked Pairs"), and skipping any pairs that would create a cycle.

In general, cycles are rare in real life and Condorcet winners usually exist, so the most important part of ranked pairs for voters to understand is simply that their rankings are used to compare candidates to each other one by one. Each pair in a ranked pairs election can be displayed in a table, like those you see if you look through the results page on Donut. The locking in of each pair can be displayed as a directed graph.

I hope this helps students better understand and appreciate their voting systems, and that students in houses with older voting systems might consider updating them. Voting, after all, is a cornerstone of student self-governance and voting systems have been one example in recent memory of students using science and math to solve their own problems without any direction from administration.