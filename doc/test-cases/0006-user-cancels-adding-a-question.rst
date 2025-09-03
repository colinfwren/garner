==============================
User cancels adding a question
==============================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0006
      - 
        * https://github.com/colinfwren/garner/issues/3
        * https://github.com/colinfwren/garner/issues/18
        * https://github.com/colinfwren/garner/issues/15
        * https://github.com/colinfwren/garner/issues/24

====
Setup
====

- There's at least 2 existing questions in the system
- There's an existing reflection in the system
- A reflection reminder has been set up

.. list-table:: Steps
    :header-rows: 1

    * - Action
      - Data
      - Expected Result
    * - View the Reflection List
      - 
      - 
        * There is a Reflection in the list
        * The Reflection has a set of Questions (note them)
        * There is no prompt to add a Question in the Reflection List
        * The "Add Reflection' button is not disabled
    * - View the Settings Screen
      - 
      - 
        * The Question list contains the existing Questions
        * There is no explanation of why user needs to add a Question
        * The Reflection Reminder should be set
    * -
        * Press "Add Question" button
        * Enter text into the Question Text Field
        * Press the Cancel Button
      - 
      -
        * No Question should be added to the Question List
        * The text input should be cleared of text (press add again to verify)
    * - View the Reflection List
      - 
      - 
        * The Reflection List does not have the "Add Question" prompt
        * The existing Reflection still has the Questions that if had before
        * The "Add Reflection" button is not disabled (verify its not greyed out, don't press it)
    * - Wait until a minute after the scheduled Reflection Reminder is due to be triggered
      - 
      -
        * The Reflection Reminder is triggered (don't add the Reflection)
        * There should be an un-actioned Reflection Reminder prompt in the Reflection List
    * - Add a Reflection
      - 
      - 
        * The Reflection should contain the Questions in the Question List and not the Question that was canceled
        * The Reflection List should no longer had the un-actioned Reflection Reminder prompt
    * - Export Data
      - 
      - 
        * The Existing Reflection before the Question was canceled should show the Questions as before
        * The newly added Reflection after the Question was canceled should show the Questions in the Question List