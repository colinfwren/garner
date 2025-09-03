==========================
User deletes all questions
==========================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0003
      - 
        * https://github.com/colinfwren/garner/issues/4
        * https://github.com/colinfwren/garner/issues/18
        * https://github.com/colinfwren/garner/issues/11
        * https://github.com/colinfwren/garner/issues/24

====
Setup
====

- There's an existing question(s) in the system
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
    * - Delete all Questions in the Question List
      - 
      - 
          * The Question List has no Questions in it
          * The explanation about Questions and why they need to be there is present
          * The Reflection Reminder is shown as paused but the schedule is still shown in the UI
    * - View the Reflection List
      - 
      -
        * The Reflection List has a prompt to say there are no Questions in the System
        * The "Add Reflection" button in the header is disabled
    * - Wait until a minute after the scheduled Reflection Reminder is due to be triggered
      - 
      - 
        * The Reflection Reminder should not be triggered
        * There should not be an un-actioned Reflection Reminder prompt in the Reflection List
    * - Export Data
      - 
      - The existing Reflections should show the Questions that have been deleted in the export