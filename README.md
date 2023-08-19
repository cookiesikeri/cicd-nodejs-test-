# cicd-nodejs-test by Ikeri Ebenezer.

this is a simple nodejs app  deployted to aws, i will explain the pipeline flow below;

*Tools*:
1. version control: github
2. CI: github actions 
3. container registry: Elastic container repository (ECR)
4. container runtime: Elastic container service (ECS)
5. Auto-Testing tools: SonarQube
6. Image scanner: Trivy scanner.
7. CodeQL: CodeQL is the code analysis engine developed by GitHub to automate security checks.

*pipeline flow*:
1. push to maain branch to trigger pipeline
2. added OIDC for token security from aws IAM
3. when code is pushed to main branch, codeQL is triggered to scan code for security checks.

4. when codeQL scan is succesful, sonarqube is triggered to scan code for vulnerabilitues, code again for code smell, duplicated codes and outdated packages.
if the code doesnt meet the standard, then its been sent back as a FAILED push with reason or reasons the code was flagged and tht can be seen in the github actions page.

SUGGESTION:  in a live scenario, i normally add slack pipeline incase there is a failed push so developers can get notified easily using slack notification.

5. if code passes all this then build starts immediately.
6. after a successful build, trivy scanner is triggered to scan the docker image properly for vulnerabilities and breakage that could affect the image in production and also for security checks. 
note: trivy result is also stored in the root of the project .
7. after the scan by trivy, then image is then pushed to ECR.



# cicd-nodejs-test-
