==========================
User completes action item
==========================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0035
      - 
        * https://github.com/colinfwren/garner/issues/28
        * https://github.com/colinfwren/garner/issues/29
        * https://github.com/colinfwren/garner/issues/30

.. list-table:: Steps
    :header-rows: 1

    * - Action
      - Data
      - Expected Result
    * -
        * Add at least one Question
        * Add a New Reflection with 2 Actions added to the Action List for the Question(s)
      - 
      - There are 2 Actions in the Actions List on the Growth Tab
    * -
        * Press "New Reflection" button
        * Press one of the uncompleted Actions in the Action List that is shown under the Question 
      -
      - The Action should be marked as completed
    * - Press the "Cancel" button on the New Reflection Sheet
      -
      - The Action should not be marked as completed on the Growth tab
    * - 
        * Press "New Reflection" button
        * Press one of the uncompleted Actions in the Action List that is shown under the Question to complete it
        * Save the new Reflection
      - 
      - 
        * The Action should be removed from the Actions List on the Growth tab
        * The Action should be shown on the Completed Actions list
    * - Press "New Reflection" button
      - 
      - The completed Action should no longer be shown in the Action List for the Question it was assigned against
    * - 
        * View the Actions List on the Growth tab
        * Press the uncompleted Action to mark is as completed
      - 
      - 
        * The Action should be removed from the Actions List
        * The Action should be added to the Completed Actions list
    * - Press "New Reflection" button
      - 
      - Neither Action should be shown on the form