========================
User re-orders questions
========================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0005
      - 
        * https://github.com/colinfwren/garner/issues/5
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
    * - Re-order the Question List (press and hold Question to drag and drop)
      - 
      -
        * The Order of the Questions in the Question List changes based on the drag and drop
        * The explanation about Questions and why they need adding is not shown as have Questions in the Question List
        * The Reflection Reminder is still active and the schedule is still shown in the UI
    * - View the Reflection List
      - 
      - 
        * The Reflection List does not have the "Add Question" prompt
        * The existing Reflection still has the Questions in the order that it had before the re-order
        * The "Add Reflection" button is not disabled (verify its not greyed out, don't press it yet)
    * - Wait until a minute after the scheduled Reflection Reminder is due to be triggered
      - 
      - 
        * The Reflection Reminder is triggered (don't add the Reflection)
        * There should be an un-actioned Reflection Reminder prompt in the Reflection List
    * - Add a Reflection
      - 
      - There Reflection should have the Questions in the new order in the Question List
    * - Export Data
      - 
      - 
        * The Existing Reflection before the re-ordering should show the Questions in the order before the re-ordering
        * The newly added Reflection after the re-ordering should show the Question in the new order