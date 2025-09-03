==============================================================
User updates a reflection when the refleciton list is filtered
==============================================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0022
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
    * - Filter the Reflection List using the term "both'
      - 
      - 
        * The first Reflection is shown
        * The second Reflection is shown
    * - 
        * Open the first Reflection
        * Remove the term "both" from the answer text
        * Press the back button in the Reflection Detail header
      - 
      - 
        * The Reflection List is still filtered
        * The first Reflection is not longer shown
        * The second Reflection is shown
    * - Clear the filter
      - 
      - 
        * The first Reflection is shown
        * The second Reflection is shown
    * - Filter the list by the term "both"
      -
      - 
        * The first Reflection is not shown
        * The second Reflection is shown
    * - 
        * Open the second Reflection
        * Update the answer text to not include the term "both"
        * Press the back buitton in the Reflection Detail Header
      - 
      - 
        * The Reflection list remains filtered
        * The second Reflection is no longer shown
        * The user sees a "no results' view