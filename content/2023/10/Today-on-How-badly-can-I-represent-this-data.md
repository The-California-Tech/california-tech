---
title: 'Today on: How badly can I represent this data'
authors:
  - Lilia Arrizabalaga
date: 2023-10-03T07:00:00.000Z
categories:
  - Editorial
tags:
  - 'Vol. CXXVII, Issue 2'
weight: 0
show_thumbnail: true
thumbnail: /img/2023/10/surface.svg
images:
  - /img/2023/10/surface.svg
sidebar: right
toc: false
widgets:
  - write-for-the-tech
  - editorial
  - taglist
  - categories
  - recent
summary: >-
  What a lovely 3-D surface plot. You can really tell that there’s data there
  and some of it is different from the other data. Place your bets now about
  what data it is!
---

Figure 0. Mmm tasty data I wonder what it measures.

What a lovely 3-D surface plot. You can really tell that there’s data there and some of it is different from the other data. Place your bets now about what data it is!

 

If you guessed The Total Number of Seats in Limited Enrollment Advanced Humanities Classes (a.k.a. “hums”) from 2007 to 2022, separated by term, you were correct! 

Each term, during the week preceding class registration for undergraduates, a common cry is heard: “There aren’t enough hums!” Much of registration day is spent consoling friends who didn’t get into the humanities course they wanted. But are these complaints warranted? Are there enough humanities classes for undergraduates to take? What does the data support?

![](/img/2023/10/advanced_seats.svg)

Figure 1. Total number of seats in limited enrollment advanced humanities classes.

![](/img/2023/10/advanced_classes.svg)

Figure 2. Total number of advanced humanities offered by year and term.

 

The data does not seem to support this claim; there are the same number of advanced humanities offered this term (FA 2023) as there were fall term last year (FA 2022) (figure 2), although there is a slight decrease in the total number of seats (figure 1). There are also a similar number of seats and classes as there were in SP 2023.

 

A quick note on terminology: here, Advanced Humanities (“advanced hums”) are 9-unit courses numbered 90 and above in English (En), History (H), History and the Philosophy of Science (HPS), Humanities (Hum), Music (Mu), Philosophy (Pl), and Visual Culture (VC) that can be taken on grades as per the Caltech Course Catalog. First-year Humanities (“frosh hums”) are 9-unit courses numbered below 60 in En, H, Pl, and VC. Students must take 18 units (2 classes) of frosh hums and advanced hums.

**\[Correction: The maximum number for frosh hums has changed throughout the years: it was 10 and below for 2007-2008, 20 and below for 2008-2015, 50 and below for 2016-2019, and has been 60 and below since the 2021-2022 academic year. However this does not impact the data as it was already filtered by being in the humanities department.]**

If you compare the number of humanities in FA 2023 to WI 2022 or to 2021, as shown in figure 2,  there is a decrease, but historically there does not seem to be a trend supporting the claim that there are too few humanities offered this term. It is interesting to note that fall terms usually have the fewest number of Advanced Humanities available, likely due to less demand (the first-year class will not yet be taking Advanced Humanities).

 

So onto the claim that there are not enough spots in advanced humanities: if we assume ~1000 undergraduates and ~250 first-years, there are ~750 upperclassmen who might want to take an Advanced Humanities course during fall term. Over 10 total terms (12 minus the two required for frosh hums because they are prerequisites for other humanities), they must take two Advanced Humanities, so around 1/5 of the upperclassmen (~150 students) are likely to be taking an Advanced Humanities course during fall term. There are ~250 spots this term which means there is ample space for students to satisfy their requirements.

![](/img/2023/10/frosh_classes.svg)

Figure 3. Total number of First-year Humanities offered by year and term.

![](/img/2023/10/frosh_seats.svg)

Figure 4. Total number of seats in limited-enrollment First-year Humanities classes.

 

Contrary to the number of Advanced Humanities, the total space in First-year Humanities has increased this year (figure 4). However, there is still not enough space to accommodate the entire first-year class (216 seats, 268 first-years). Because you must take an average of one humanities class per term and you cannot take more Advanced Humanities until you take First-year Humanities, this is unideal as it will result in more people needing to take 2 humanities in a term.

Methodology: I used a Python script to scrape course data from termly course schedules pages on schedules.caltech.edu (which only goes back as far as 2007). There were a handful of Advanced Humanities classes which did not have limited enrollment (none this term and no more than 5 total) and when calculating the total seats I omitted those classes (I did not omit them from the total number of classes). If you want to see my data or code, you can contact me at [larrizab@caltech.edu](mailto:larrizab@caltech.edu). [https://github.com/Dominus-Draconis/caltech\_hums/](https://github.com/Dominus-Draconis/caltech_hums/) 
