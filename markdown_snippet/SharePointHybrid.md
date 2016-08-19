本章旨在给用户一个好的动手实践概况，来检测和解决 Hybrid SharePoint 配置中经常会遇到的各种问题。这不是用来替代 Microsoft Customer Support Services 的，
但我们希望它能帮助您解决大部分问题。如果您想新开一个 Micosoft Customer Support Services case，您在本章将会学到的建议和技术将会指引你如何提供
给 support engineer 所需要的诊断信息。

介绍
====
当微软在培训 customer support oganization 的 support engineer 时，他们被告知需要做的第一件事情便是恰当地找出他们需要解决的问题。这包括定义
错误产生的条件的性质，以及更重要的是，如何定义问题被解决的标准来使各方满意。当您在解决问题的时候，我们强烈建议你使用相同的方法，考虑下你
手中的问题的 scope。不管你遇到什么问题，这会帮助你 home in 到可能的原因。到现在位置，本书的中心都在关键的 hybrid SharePoint 和 Microsoft 
Office 365 架构上，如您需要，可以查阅之前的章节来定和隔离您遇到的问题。

当您阅读本章的时候，我们将会遵循一个类似的方针，先从基础开始到诊断过程中的处理，然后提供真实的例子和场景。这个方法会帮助您诊断并解决在部署
SharePoint on-premises and SharePoint Online as a hybrid solution 过程中可能会遇到的问题。

诊断方法
========
许多 customer 向 Microsoft Support 提出的问题都可以分为常见问题和部署错误。当面临这一个崩溃的 hybrd 部署环境时，有一个更好的诊断方法。这个
诊断方法基于排除法，先从最容易发生问题开始排除，然后是次频繁发生的问题，知道我们找到问题的根本原因。在某些情况下，修复一个问题会带来另外一个
问题，所以把问题按不同的领域区分开来就特别重要了，而不是提供一个万能的一站式解决方案。

让基础设施能够工作
=================
当我们回顾早期 Office 365 和 SharePoint 的 Hyrid 部署的日子，有一些问题比另外一些问题发生得更频繁。总之就是这些问题都是属于 hybrid 部署中的
的某个关键元素没配置好：让基本的必备条件正确地满足好，特别是 identity 条件。所以我们在诊断问题的这章中先从验证 identity management 被正确地
设置好了的一些最佳实践开始，然后接下来才是真正的 hybrid 问题。

验证 directory 同步
===================
