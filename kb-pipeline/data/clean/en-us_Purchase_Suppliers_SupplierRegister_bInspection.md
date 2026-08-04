### Inspection
In this box you decide if receiving inspection should be applied for parts on purchase orders from the supplier.

#### Receiving inspection
With this setting you determine if receiving inspection should be applied. The following options are available:
- No – Receiving inspection will not be applied.
- Yes – Receiving inspection will be applied.
- Interval – Variable receiving inspection will be applied. You configure settings for this via the Inspection settings button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) (see below) next to the field.
-   
The Inspection settings button
If Receiving inspection is set to Interval, this button becomes available. Here you can configure settings regarding variable receiving inspection. This is done by selecting an Inspection template. Inspection templates first have to be created in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – SRM procedure.
The inspection templates are used to trigger receiving inspection under different circumstances, for example, if parts on purchase orders from the supplier have been given a new revision, if a case is registered, or if previous receiving inspections have resulted in rejections.
In the dialog window you see all of the settings for the inspection template. Level shows the current inspection level of the inspection template. By using the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add.png) and ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_reject.png) buttons you can step up/step down the current level in the inspection template. You can see the settings on each level in the inspection template. You can see the number of performed inspections on parts from the supplier. By using this button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png) you can reset the number of performed inspections to 0.00. If an inspection template is selected, the value for Frequency is loaded from the first row in the template. This cannot be updated. When the next level in the template has been reached, the value is loaded from the inspection template.
> Changes made for inspection templates in either the Basic data – Part or Basic data – SRM will not affect parts or suppliers which have already been assigned the inspection template in question.

#### From
If Receiving inspection is set to Yes or Interval, this field becomes available and today's date is suggested. Here you can select a date from when the receiving inspection should be applied for the supplier.

#### To
If the Receiving inspection is set to Yes or Interval, this field becomes available. Here you can select a date to when the receiving inspection should be applied for the parts being arrival reported from the supplier.

#### Instruction
If the Receiving inspection is set to Yes or Interval, this button becomes available. Here you enter an instruction regarding the receiving inspection. The text you enter here will be shown to the person performing the inspection. The instruction will still be there if you deactivate the receiving inspection, and then activate it again.
By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Files
If the Receiving inspection is set to Yes or Interval, this button becomes available.
By clicking the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png), it is possible to link different files related to a comment or an instruction for the record in question. When the setting Automatic printout is available for activation, you can choose to get the linked file automatically printed. Read more in the topic [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles) about how to link files, automatic printout, and where linked files can be automatically printed. If there are linked files, you will see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_linked.png) on the button.
Files you link here can e.g. be check lists or measuring records regarding the receiving inspection, and they are also displayed for the person performing the inspection. If you check the Automatic printout box when linking a file, that file will be automatically printed when you save the arrival reporting. This way the printout will be available in the next step, that is, the receiving inspection. Linked files will still be available if you deactivate the receiving inspection, and then activate it again.
Viewing of PDF files is supported.Using the option Extended file viewer you can view/show more file types, such as different drawing formats and Office formats. By clicking this link you access a complete list of the [supported file formats](https://www.rasterex.com/file-formats?hsCtaTracking=f7142bf7-4cfa-4c3b-8be8-cde24df7f2b4%7Cdae7ecbb-26b0-43cd-b9d0-3579248ec31b).
