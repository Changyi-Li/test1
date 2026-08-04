### 页眉行

#### 拣货单号
在这里你可以选择或输入需要已包装的拣货单。拣货单是创建自列表类型创建的 拣货计划 在里面 交货计划 程序。

#### 预留/取消预留
使用按钮 预留 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_release.png) 和 取消预留 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_undo_release.png) 你可以对拣货单中的全部组件执行预留或撤销预留。
默认下，预估拣货单上的全部组件未预留，并且拣货单状态 页眉 框然后显示“预估”。
默认下，常规的拣货单拣货单状态的全部组件均已已预留，并且 页眉 箱子然后变为“交货就绪”状态。如果你撤销交货就绪的拣货单的预留，拣货单状态将被重置为“预估”。

#### 包装就绪 （包装结构已准备好交货）
在这里你选择 是的 当全部包装都已完全已包装并交货就绪。这然后设置 完成的 在包装结构中的全部行上（如果不在行上人工的输入）。
> 当设置 包装就绪好交货 被设定为 是的，你否再更改 包装结构 盒子。但即使拣货单已经已交货，仍有可能对其进行变更。然后你应该将此字段设置为 否 这样，在你选中该复选框之后，就可以变更包装结构 完成的 在该框中应该已变更的行上。例如，你可以更改毛重，添加/删除包装行或组件行，更改数量。

#### 电子数据交换
点击 电子数据交换 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 你可以看到有问题的EDI 信息。
在里面 EDI 已连接 它说的字段 是的 如果拣货单上的客户已连接到 EDI，否则它将阅读 否。默认值是从客户加载的。当客户连接到 EDI 时，可以使用 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 字段下一个的按钮可查看应用于该客户的EDI 事务类型和方向。
如果客户连接到 EDI，则可以发送EDI通知。这是通过使用 通过 EDI 发送 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_send_edi.png) 该命令然后可在程序工具栏上可用。默认交货单发货通知已发送打印在 报告交货 或者 打印交货文档 程序。当已发送发货通知时，它是根据与客户已链接的EDI 行为进行的。这可以在程序 管理 EDI 事务。
如果客户已连接到 EDI，你可以使用设置 排除自 EDI 决定是否应将相关拣货单发货通知排除在 EDI 流之外。这意味着发货通知不能通过上面程序通过 EDI已发送。这 通过 EDI 发送 按钮然后将被未激活。
你还可以看到 EDI 导出状态 用于显示导出日期和时间的发货通知。
