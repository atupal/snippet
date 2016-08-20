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

我们不推荐在 MIISClient 工具中修改密码，除非您对 Microsoft Identity Management 产品有深入的理解。相反，我们推荐运行 Azure AD Connect Configuration 工具，然后提供更新后的凭证。

当您确信 directory synchronization 正确地工作了并且在 Office 365 Admin Portal 的 DirSync tile 上没有任何错误信息之后，就可以进入下个诊断的步骤了。

验证 Azure Access Control Services server-to-server trust
=========================================================
SharePoint Server 和 Office 365 的 hybrid workloads 的核心是一个桥接 on-premiese 和 Online 环境的配置元素。Windows Azure Active Directory Access Contrl Service (ACS) 是一个基于云的 federation service，它提供了一种易用的方式来对 identiy providers 来认证用户，最重要的 identiy provider 便是 Azure Active Direcotory。因为 ACS 是所有 hybrid 场景的核心，如果它出了毛病会影响到所有的工作。第一章已经描述过如何配置 ACS，您可以一步一步地按照着配置。这也意味着我们同样也可以一步一步地去验证所有的一切都在正常工作。实现验证的最好的方式就是使用 Windows PowerShell。

您可以使用下面的脚本块来验证 server-to-server (S2S) trust，ACS 被正确配置好了。

首先，让我们确保有足够来进行诊断。这将包含一个被创建或者从某处获取到的原先用于配置 ACS trut 的证书。我们还需要 Offie 365 SharePoint Online App ID。
> Note 如果您使用了 Hybrid Picker 或者 Cloud Search Service Application onboarding script，您不会有这个证书。在这种情况下，我们可以安全地假定脚本将会是一致的，因为它就是我们用来配置 trust 的同一个证书。

当您创建或者获取一个证书时，您需要确认它正在被 SharePont on-premises 用于对 token 签名。您可以比较证书的拇指纹是否一致来判断。

这个脚本的输出将会显示正在匹配证书的拇指纹。

您接下来需要验证用于 token 签名的证书没有过期。如果过期了，将会导致 token 签名问题，通常表现为在用户界面或者 Unified Loging Service (ULS) 日志中出现 JWT token 错误。

这个阶段的输出将会显示当前的证书和可能已经被替换了的以前部署的证书。下面的例子显示了两个注册到 Office 365 Application Principal 的两个证书。其中一个已经过期了，另外一个是更新的一个证书且过期时间更长。仅供参考，一个过期时间为 1/1/999 的 hybrid 证书通常表示内置的 SharePoint Security Token Signing Certificate 被用来组成 trust。如果您没有任何用于 ACS trust 的合法证书，您必须得部署一个新的。您可以依照第一章中相关的步骤来部署一个新的证书，或者重新运行 Hybrid Picker 或者 Cloud Search Servide Application onboarding script 来重新创建 trust。

为了让 ACS 配置工作，您下一件需要检查的事情是验证注册到 Office 365 application principal 上的 Service Principal Names (SPNs) 和期望的 on-premises 用户请求的来源是一致的。

脚本的输出显示了一个或多个 SPN，这些 SPN 涵盖了 outbound request 会收到和 inbound request 会被发送的 SharePoint web appliation URL。在下面的例子中，您可以看到 SPN 是一个匹配 *.contoso.com 的通配符。这个通配符意味着所有的 full qulified domain name (FQDN) 以 contoso.com 结尾的 web application 都会被这个 SPN 所覆盖。

对 SPN 需要小心的一点不要让多余的 SPN 覆盖同同样的 URL。举例来说，如果从脚本的输出是下面这样的，我们就有了一个重复的 SPN 冲突，因为通配符已经覆盖了所有的可能性，intranet.contoso.com 这个显示的 SPN 就不再需要了。这是我们应该避免的。

要移除一个重复的 SPN，您可以使用下面的脚本：

这里的索引值(1)，应该被替换成需要移除的 SPN 的 ID。在前面的例子中，这会移除掉 intranet.contoso.com 这个 SPN 而留下通配符。这是因为通配符可能还会被用于其他的目的，但是通配符也覆盖了我们正在移除的 SPN，所以不会功能上的丢失。

验证 ACS trust 被正确设置的最后一步就是确保 ACS ServiceApplicatinProxy 已经被成功地部署好了。SharePont 通过 ServiceApplicationProxy 来和 ACS service endpoint 通信，所以确保它被部署了且在线对 ACS trust 实现是非常重要的。

脚本的输出应该显示 proxy 在线和它配置的 ACS endpoint。

这个时候另外一个额外的诊断验证步骤是检查 on-premises SharePoint 服务器能够访问 MetaDataEndpointUri。如果您把这个 URL 复制到浏览器中并打开，一个下载文件，1.json，的对话框应该会弹出到您的面前，这个文件包含了证书和一些关键细节，这对 Microsoft Support 诊断来说可能会很有用。如果您不能访问这个文件，您应该检查服务器能够访问外网。

单独验证证书
============
我们当前的主题是证书，对证书进行通常的检查值得一看。如果您怀疑或者有证据表明证书因为一些原因可能损坏了，您可以使用 Active Directory Certificate Services tool, CertUtil.exe, 来进行证书验证。CertUtil.exe 有许多特性，您可以在 https://technet.microsoft.com/
library/cc732443.aspx 阅读更多，但在这一章中，我们关注的只有一个：验证。

用管理员的身份运行下面的命令行：

这里的输出被重定向到 certverfiy.txt 文件中去了，您可以检查这个文件，查看是否有证据表面这个证书出现了问题。在这个例子中，我们故意检查了一张已经过期了的证书，这是最常见的错误。certverify.txt 文件的内容看起来会像下面这样：

