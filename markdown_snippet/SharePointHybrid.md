本章旨在给用户一个好的动手实践概况，来检测和解决 Hybrid SharePoint 配置中经常会遇到的各种问题。这不是用来替代 Microsoft Customer Support Services 的，但我们希望它能帮助您解决大部分问题。如果您想新开一个 Micosoft Customer Support Services case，您在本章将会学到的建议和技术将会指引你如何提供给 support engineer 所需要的诊断信息。

介绍
====
当微软在培训 customer support oganization 的 support engineer 时，他们被告知需要做的第一件事情便是恰当地找出他们需要解决的问题。这包括定义错误产生的条件的性质，以及更重要的是，如何定义问题被解决的标准来使各方满意。当您在解决问题的时候，我们强烈建议你使用相同的方法，考虑下你手中的问题的 scope。不管你遇到什么问题，这会帮助你 home in 到可能的原因。到现在位置，本书的中心都在关键的 hybrid SharePoint 和 Microsoft Office 365 架构上，如您需要，可以查阅之前的章节来定和隔离您遇到的问题。

当您阅读本章的时候，我们将会遵循一个类似的方针，先从基础开始到诊断过程中的处理，然后提供真实的例子和场景。这个方法会帮助您诊断并解决在部署SharePoint on-premises and SharePoint Online as a hybrid solution 过程中可能会遇到的问题。

诊断方法
========
许多 customer 向 Microsoft Support 提出的问题都可以分为常见问题和部署错误。当面临这一个崩溃的 hybrd 部署环境时，有一个更好的诊断方法。这个诊断方法基于排除法，先从最容易发生问题开始排除，然后是次频繁发生的问题，知道我们找到问题的根本原因。在某些情况下，修复一个问题会带来另外一个问题，所以把问题按不同的领域区分开来就特别重要了，而不是提供一个万能的一站式解决方案。

让基础设施能够工作
=================
当我们回顾早期 Office 365 和 SharePoint 的 Hyrid 部署的日子，有一些问题比另外一些问题发生得更频繁。总之就是这些问题都是属于 hybrid 部署中的的某个关键元素没配置好：让基本的必备条件正确地满足好，特别是 identity 条件。所以我们在诊断问题的这章中先从验证 identity management 被正确地设置好了的一些最佳实践开始，然后接下来才是真正的 hybrid 问题。

验证 directory 同步
===================
在您使用任何 hybrid 部署场景之前，将会参与进来的用户和组的 identities 同步到 Azure Active Directory 十分重要，你可以使用某个被支持的工具来实现同步。在这个阶段，我们假定目录同步已经成功地发生过了，所以这里我们将会寻找那些部署后的问题。

> 所有的 Office 365 tenant 体验将只会使用新的 modem tenant admin page 来描述。在写本书时候 modem portal 已经有预览版了，但是需要点击当前的 admin potal 的一个链接进去，您可以访问  https://portal.office.com/adminportal/home?switchtomodern=true#/homepage 进入。

检查 directory syncronnization 是否出现问题的第一个地方便是登录进 Office 365 Admin Center 并检查 Dashboard 页面。Dashboard 上有一个 tile 显示了 directory syncronization 的状态（图 6－1），这个状态表示了 directory syncronization 的健康状态。在进行任何其他步骤之前您应该保证 directory syncronization process 是健康的。如果在 Dashboard 上没有这个 tile，说明 direcotyr syncronization 没有在当前的 tenant 打开。您应该按照这个指南来配置好它：[Planning and Preparing for Microsoft SharePoint Hybrid](https://blogs.msdn.microsoft.com/microsoft_press/2016/04/26/free-ebook-planning-and-preparing-for-microsoft-sharepoint-hybrid/)。没有 directory syncronization，所有的 hybrid 场景都会失败。

图 6-1 Office 365 Admin Portal 的 DirSync 状态 tile。图中显示的是一个健康的状态。

如果 directory syncronization tile 显示的是一个错误或者警告的状态，如图 6-2 所示，说明 directory syncronization 打开了但是由于一些原因失败了。

图 6-2 Office 365 DirSync 状态 tile 显示了一个非健康的状态。

在这个时候，你可以点击最后一条 Directory Sync 错误信息进入 Directory Sync 的状态页面。这个页面包含了有用的管理信息。图 6-3 显示的是一条警告信息：正在使用较老版本的 DirSync client。现在还不会造成问题，但微软将会在 2017 年停止对老版本的同步客户端的支持，所以我们建议升级到最新的版本。在状态页面上您还可以看到很多其他的关于同步的警告，并且包含 DirSYnc troubleshooting 工具的链接。DirSync troubleshooting 工具是一个 click-once 的应用，并且必须运行在 DirSync 服务器上。他有两个诊断选项：快速扫描和完整扫描。快速扫描会查看 DirSync 服务器的 event log 和 Office 365 的设置。完整扫描会更详细，并且会扫描 active directory 里的 objects 以发现潜在的错误。

图 6-3 DirSync 状态对话框

在 Directory Sync 状态页面上还另外一个有用的诊断工具的链接：IdFix 是一个 Active Directory Object 分析工具，它可以标记出可能会造成同步错误的 object 的问题。IdFix is reviewed in [Planning and Preparing for Microsoft SharePoint Hybrid](https://blogs.msdn.microsoft.com/microsoft_press/2016/04/26/free-ebook-planning-and-preparing-for-microsoft-sharepoint-hybrid/) as part of the Active Directory preparration steps.

> More Info 您可以在 https://support.office.com/article/Fixing-problems-with-directory-synchronization-for-Office-365-79c43023-5a47-45ae-8068-d8a26eee6bc2?ui=en-US&rs=en-US&ad=US 上发现更多的如何修复 directory 同步错误的阅读材料。

另外一个诊断 directory 同步问题 Microsoft Identity Integration Server (MIIS) 客服端工具(Synchronization Service Manageer Tool)，它可以在同步服务器上的 C:\Program Files\Microsoft Azure AD Sync\UIShell\MIISClient.exe 路径上找到。

图 6-4 显示了 MIISClient 给管理员快速展示了同步的状态，以及在 on-premises 和 Azure Active Directory 之间是否有任何连接和访问问题。

图 6-4：Synchroniztion Service Manager client (MIISClient.exe) 工具。

如果 on-premises Azure Active Directory Connect (Azure AD Connect） 服务器和 Office 365 Tenant 之间有任何连接错误，您会在这个客户端工具上看到。一些最常见的错误在 Microsoft TechNet guide to the MIISClient 上列出来了：https://technet.microsoft.com/library/
ee323428(v=office.13).aspx。这个指南现在已经非常老了，但它在检查错误信息上仍然是一个很有价值的资源。

对于我们来说如果要深入诊断所有的问题话未免太多了，然而，在 MIISClient 中最常见的同步错误是由 Azure Active Directory agent (contoso.onmicrosoft.com, 见图 5-4) 报告的一个状态：Stopped-Server-Down。这条信息倾向于让管理员相信是因为某个网络连接错误使得 Azure Active Directory instance 不能被连接上。这个错误的最常见原因实际上是因为在安装 Azure AD Connect 过程中指定的同步帐号的密码过期了，或者密码被修改了。有两个方法来解决这个问题：
- 重新从头开始运行 Azure AD Connect Configuration 工具
- 在 MIISClient 工具中修改帐号密码

