### Rules
In this box under the Rules tab you add the rules which should exist in the configuration group. You can also delete rules provided that they are no longer used. It is also possible to copy rules and renumber rules. Read more about this below.
By using the button Copy row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy_row.png) (Ctrl + Shift + C) you can copy a rule to create a new rule. This is useful if you are about to create many rules as you can then use one rule as a template. A window opens and there you get to enter a new rule number and you can make alterations in the new rule (read more about this window under the heading Rule definition below).
By using the button Renumber rule number ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_sort_right.png) it is possible to renumber an existing rule number. First you enter a Start value. In the field From rule number, you then select from which rule number the renumbering should be done. If you want all rules in the table to be renumbered, you can leave the field To rule number empty. Otherwise you enter to which number the renumbering should be made. Finally you enter a value in the field Increase with. This is how much each number should be increased with.

#### Rule number
Each rule is given a rule number starting with 1000, 1001, 1002, etc. But it is possible to enter another rule number. It is also possible to renumber the rule numbers (see above).
> It might be good to divide the rules with different number series in order to create a logical division.

#### Description
Here you enter a description of the rule. This description makes it easier to find and to understand the rules which have been created.

#### Rule definition
By using the button Rule definition ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/gridFolderImage.png) you open a window with the same name, where you create the rule definition. Please see the explanations below regarding the different sections in the window.
Structure map
In this section you see the entire structure of the configuration group. Here you see which sections, option lists with options (parts), and variables, that are included in the configuration group. It is possible to drag components from the structure map and drop them in the different boxes in the window, and this way easily create the rules.
Definition
In this section you add the rule definition. This definition is the terms that should fulfilled in order for the rule to be applied.
You set up what should happen when the rule is applied in the section Affected components.
In the rule definition it is possible to mix options and variables, and to create complex terms using the operators Either or and All, see below. A validation is made of the settings you configure, to see that the rule does not become invalid.

#### Operator
An operator can be All (And), Either or (Or), Option, or Formula. You can add multiple operators and also add operators in sub-levels.
Example with one term:
"If a certain option has been selected, something should happen". It is appropriate to on the first row (the top row) always have the operator Either or, if you in the future should want to expand the term. Then you should, on an underlying level, add a row with the term that must be selected in order for the rule to be used.
Example when it is sufficient with one out of several terms:
"If one out of several options has been selected, something should happen". Then you also use the operator Either or and add on rows on an underlying level, the terms of which at least one must be selected in order for the rule to be used.
Example when all terms must be fulfilled:
"If all options have been selected, something should happen". Then you use the operator All and add on rows on an underlying level, the terms which must be selected in order for the rule to be used.

#### Negation
If you check the Negation checkbox, the operator will become excluding (that is, the logical expression Not). This checkbox is by default not checked.
> Negation can be efficient if a rule should always be true, except for when a specific option has been selected. Then it is enough that you create a rule only for this option and activate Negation for that term, instead of creating a rule where you add all other options as terms.

#### Option list
If the operator is set to Option you should here select the option list.

#### Option
If the operator is set to Option you here select an option in the option list in question.

#### Formula for rule f(x)
If the operator is set to Formula you will here see a button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_formula.png) where you enter the rule formula. This must be used when variables should be included in the rule definition.
> You can start a row with /// if you want to write a comment for your formula.

#### More info
Under the button More info ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), the option list and name are displayed.
Affected components

#### Excluded by rule
Here you add option lists, options, and variables, which should be excluded by the rule. For an option list it is possible to select one option. If you do not select an option, the entire option list will be excluded.

#### Selected by rule
Here you add options to option lists which should automatically be selected by the rule. You must select one option in each option list.
Logical formulation
In this section you see the rule definition's logical formulation in code. Option lists are shown with option list codes, options are shown with part numbers, and variables are shown with variable codes. Formulas are shown in plain text as they are displayed in the formula editor.
For example, if the rule has one row with an option list and one option you will see the code: IsSelected(option list code|part number).
If Negation is activated on the row then you will see the code: not(IsSelected(option list code|part number)).
If the rule has a row with an option list and an option as well as a row with an option list and a variable, and the operator is Either or you will see the code: (IsSelected(option list code|part number) or IsSelected(option list code|variable code)).
If the operator in the example above is All you will see the code: (IsSelected(option list code|part number) and IsSelected(option list code|variable code)).

#### Logical formulation
In this column you see the rule definition's logical formulation as code, in the same way as in the section Logical formulation under the button Rule definition.
It is possible to filter by values in this column and in the following two columns and in this way you can for example fin all rule in the tab where a certain option is used.

#### Excluded by rule
Here you see the option lists, options, and variables, which are excluded by the rule.

#### Automatically selected by rule
Here you see the options in option lists which automatically are selected by the rule.
