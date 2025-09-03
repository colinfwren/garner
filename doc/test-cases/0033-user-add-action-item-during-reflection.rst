=======================================
User adds action item during reflection
=======================================

.. list-table:: Metadata
    :header-rows: 1

    * - Test ID
      - Covered User Stories
    * - 0033
      - 
        * https://github.com/colinfwren/garner/issues/28
        * https://github.com/colinfwren/garner/issues/29

.. list-table:: Steps
    :header-rows: 1

    * - Action
      - Data
      - Expected Result
    * -
        * Create at least 1 Question
        * Press "Add Reflection" button to add a new Reflection
      - 
      - 
        * New Reflection sheet is shown
        * Question(s) that were added are shown on the Reflection form
        * Under the Question(s) input is an "Actions" list with a button to add a new Action
    * - Press "Add' button on the Action List
      - 
      - 
        * Sheet should pop up with an input to add action
        * Input to add action should be focused
        * Buttons shown for canceling the adding of an action and saving it
    * - 
        * Enter text into the Action input
        * Press Cancel
      - 
      - No action should be added to the action list
    * - Press "Add" button on action list again
      - 
      - 
        * Action input should be empty
        * Action input is focused
    * - 
        * Enter text into action input
        * Press Save button
      - 
      - Action that was entered is added to the Action List under the question it was triggered from
    * - Press Cancel on New Reflection Sheet
      -
      -
        * No Reflection is created
        * Actions created during Reflection creation aren’t saved either
    * - 
        * Press "New Reflection" button again
        * Press "Add' button on an Action List again
        * Enter Action name in input
        * Press Save to add the Action to the Action List
        * Press Save on the New Reflection Sheet’s options
      - 
      - 
        * The new Reflection is saved
        * The Action that was added to the Action List is saved
    * - View the Growth tab
      - 
      - The newly added action should be shown on the Action List
    * - Press "New Reflection" button again
      - 
      - Under the Question that the action was created under the action should be shown