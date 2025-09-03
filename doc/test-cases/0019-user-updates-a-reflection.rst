=========================
User updates a reflection
========================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0019
      - 
        * https://github.com/colinfwren/garner/issues/17

====
Setup
====

- There's an existing question in the system
- There's at least 1 existing reflection in the system

.. list-table:: Steps
    :header-rows: 1

    * - Action
      - Data
      - Expected Result
    * - Export Data
      - 
      - Reflections to be updated is included in the exported data
    * - View Reflection List
      - 
      - 
        * There are at least 1 Reflection in the Reflections List
        * The Reflection List can be filtered
        * Reflection to be updated in in the Reflection List
        * The user does not see the "Add first Reflection" prompt in the Reflection List
    * - Filter Reflection List using text found in the Reflection to be updated
      - 
      - Reflection to be updated is in the filter results
    * - 
        * Ensure the Reflection List is not filtered
        * Press the Reflection to be updated
        * Amend the answer text in the Reflection so that it no longer has the text used to filter the list in previous steps
        * Press back in the header
      - 
      - 
        * Reflection is updated in the Reflection List with the new answer text
        * User does not see the "Add First Reflection" prompt
    * - Filter the Reflection List using the term that was present in pre-updated Reflection but was removed when the Reflection was updated
      - 
      - 
        * The Reflection that was updated is no longer shown in the results
        * If there are no other matches then the "No Results" screen is shown, or the other Reflections that match that term are shown
    * - Export Data from App
      - 
      - The Reflection that was updated is shown with the updated answer text in the export