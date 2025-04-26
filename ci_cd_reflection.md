CI (Continuous Integration):  
A practice in software development where developers frequently integrate code into a shared repository. Each integration is verified by automated builds and tests.  

CD (Continuous Deployment):  
Automates the release of validated code to production. After passing CI checks, the code is deployed with minimal manual intervention.  
Its used to catch bugs early, encourages collaboration, reduces integration issues, speeds up development and release cycles.  

## Purpose  

The goal of continuous integration and deployment (CI/CD) is to streamline and automate the software development lifecycle. CI guarantees that code changes are routinely incorporated into a shared repository, where automated builds and tests are executed. CD goes a step further, automatically delivering code to production or staging environments. This process enables teams to identify issues early on, maintain uniform code quality, and deliver features faster and more reliably.   

Automating style checks such as linting and spell checking helps to ensure uniform formatting and writing quality across a codebase or page. These tests detect minor but significant errors (e.g., typos, markdown formatting difficulties) before they are merged, lowering technological debt and enhancing readability. It also saves time during code reviews because developers do not have to manually highlight stylistic mistakes.

## Challenges  

* False positives: Tools may identify issues that do not exist.

* Configuration complexity: Setting up CI workflows and tools such as Husky or GitHub Actions can be difficult, especially across multiple operating systems.

* Developer friction: Strict restrictions may frustrate team members, particularly if the checks hold down commits or PRs.

* Tool compatibility: It can be difficult to ensure that all team members have the same versions of linting or spell-check tools installed.

In small projects, pipelines are usually simpler and focus on basic tasks like linting, testing, and building. The goal is to keep things light and fast. A single developer might maintain the pipeline.

## Difference between small projects and large teams  
In large teams, pipelines can be much more complex. They often include multiple stages (build, test, security scan, deploy, integration tests), parallel jobs, and environment-specific workflows. There may also be approval gates, monitoring hooks, and rollback mechanisms. Large teams may dedicate DevOps engineers to maintain and optimize these workflows.
