========================================================
User is shown the Add Question prompt in reflection list
========================================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0024
      - 
        * https://github.com/colinfwren/garner/issues/3
        * https://github.com/colinfwren/garner/issues/21

====
Setup
====

- There's no questions in system
- There's no reflections in system

.. list-table:: Steps
    :header-rows: 1

    * - Action
      - Data
      - Expected Result
    * - 
        * Delete any Questions in the system
        * Delete any Reflections in the system
      -
      -
        * There a no Questions in the Question List
        * There are no Reflections in the Reflections List
    * - View Settings Screen
      - 
      - There is an explanation around why Questions are needed to be present to add a Reflection
    * - View the Reflection List
      - 
      - 
        * There is a prompt to add a question in order to add a Reflection
        * The "Add Reflection" button in the header is disabled
    * - Press the "Add Question" prompt
      - 
      - 
        * The user is taken to the settings screen
        * The Add Question Sheet is shown
        * The Question input field is focused
    * - Add a Question
      - 
      - 
        * The Question List contains the newly added Question
        * The Question List no longer has the explanation on why need to add Questions
        * A "Add your First Reflection" prompt is shown under the Question List
    * - View the Reflection List
      - 
      - 
        * The "add Question" prompt is no longer shown
        * The "Add Reflection" button is no longer disabled
        * There is a "Add your first Reflection" prompt in the Reflection List
    * - Add 10 Reflections
      - 
      - 
        * The Reflection list has the search bar shown
        * There are 10 Reflections in the Reflection List
    * - Delete all the Questions
      - 
      - 
        * The Question List has no Questions in it
        * The explanation about why need Questions to add Reflections is shown again
    * - View the Reflection List
      - 
      - 
        * The Search bar is shown
        * There are 10 Reflections in the Reflection List
        * The "Add Question" prompt is shown again
        * The "Add Reflection" button is disabled again