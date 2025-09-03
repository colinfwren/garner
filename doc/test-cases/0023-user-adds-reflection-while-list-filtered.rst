===========================================================
User adds a reflection when the refleciton list is filtered
===========================================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0023
      - 
        * https://github.com/colinfwren/garner/issues/20

====
Setup
====

- There's an existing question in the system
- There's 2 reflections in the system

.. list-table:: Steps
    :header-rows: 1

    * - Action
      - Data
      - Expected Result
    * - 
        * Ensure that there are 2 Reflections in the system
        * 1st Reflection
          * has the word "filter" in the answer text
          * does not have the term "search" in the answer text
          * has the word "both" in the answer text
        * 2nd Reflection
          * has the word "search" in the answer text
          * does not have the word "filter" in the answer text
          * has the word "both" in the answer text
      - 
      - The Reflection List has those two Reflections
    * - Ensure that the Reflection Reminder notification will trigger in 2 minutes time
      -
      - 
    * - Filter the Reflection List using the term "neither"
      -
      -
        * The first Reflection is not shown
        * The second Reflection is not shown
        * The user sees the "no results" view
    * -
        * Wait for the Reflection Reminder to have triggered
        * Select "Add Reflection" on the alert that is shown to show the Add Reflection Sheet
        * In the Add Reflection Sheet enter "neither" in the answer text
        * Press Save on the Add Reflection Sheet
      - 
      - 
        * The reflection list remains filtered
        * The newly added Reflection is shown
        * The first and second Reflections are not shown
        * The user no longer sees the "no results" view
    * - Clear the filter
      - 
      -
        * The first, second and third Reflections are shown
        * There is no un-action Reflection Reminder prompt shown in the Reflection list