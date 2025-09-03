================================================================
User is shown the Add First Reflection prompt in reflection list
================================================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0025
      - 
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
    * - Add a Question
      - 
      - 
        * The Question List contains the newly added Question
        * The Question List no longer has the explanation on why need to add Questions
        * A "Add your First Reflection" prompt is shown under the Question List
        * A "Add your First Reflection" prompt is shown on the Reflection List
    * - Press the "Add your first Reflection" prompt under the Question List
      - 
      - 
        * The UI switches tabs to the Reflections tab
        * The user is shown the Add Reflection Sheet
    * - Save the Reflection
      - 
      - 
        * The Add Reflection Sheet is dismissed
        * The user is on the Reflection List
        * The newly added Reflection is at the top of the Reflection List
        * There are no unactioned reflection reminders in teh reflection list
    * - Delete the newly added Reflection
      - 
      - 
        * The Reflection list has no Reflections in it
        * There "Add your first Reflection' prompt is shown in the Reflection List
    * - Press the ‘Add your first Reflection’ prompt
      - 
      - The Add Reflection Sheet is shown
    * - Save the Reflection
      - 
      - 
        * The Add Reflection Sheet is dismissed
        * The user is on the Reflection List
        * The newly saved reflection is at the top of the reflection list
        * There are no unactioned reflection reminders in the reflection list