=============================
User cancels sending feedback
=============================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0031
      - 
        * https://github.com/colinfwren/garner/issues/26

.. list-table:: Steps
    :header-rows: 1

    * - Action
      - Data
      - Expected Result
    * -
        * Add at least 1 question
        * Add at least 2 reflections
      - 
      -
        * question list is populated
        * reflection list is populated
        * Provide Feedback button is shown in the Settings Screen
    * - Press Provide Feedback button
      - 
      - 
        * Feedback sheet is shown
        * Submit button is disabled (enabled by typing)
    * - Type in feedback box
      - 
      - Submit button is enabled
    * - Press Cancel button in Feedback sheet
      - 
      - 
        * No feedback is sent
        * The feedback input box is cleared
        * The feedback sheet is dismissed
    * - Press Provide Feedback again
      - 
      - The input box should be empty
  