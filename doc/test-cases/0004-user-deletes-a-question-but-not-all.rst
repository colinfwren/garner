===================================
User deletes a question but not all 
===================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0004
      - 
        * https://github.com/colinfwren/garner/issues/4
        * https://github.com/colinfwren/garner/issues/18
        * https://github.com/colinfwren/garner/issues/11
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
    * - Delete a Question in the Question list
      - 
      -
        * The Question is no longer in the Question List
        * The explanation about Questions and why they need to be there is not shown as have a Question in the Question List still
        * The Reflection Reminder is still active and the schedule is still shown in the UI
    * - View the Reflection List
      - 
      - 
        * The Reflection List does not have the "Add Question" prompt
        * The existing Reflection still has the Questions that it had before deleting the Question
        * The "Add Reflection" button is not disabled (verify it is not greyed out, don't press it yet)
    * - Wait until a minute after the scheduled Reflection Reminder is due to be triggered
      - 
      - 
        * The Reflection Reminder is triggered (don't add the Reflection)
        * There should be an un-actioned Reflection Reminder prompt in the Reflection List
    * - Add a Reflection
      - 
      - 
        * The Reflection should not contain the deleted Question
        * The Reflection List should no longer had the un-actioned Reflection Reminder prompt
    * - Export Data
      - 
      - 
        * The Existing Reflection before the Question was deleted should show the deleted Question
        * The newly added Reflection after the Question was deleted should not show the deleted Question