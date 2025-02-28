<h2>Libraries</h2>
<ol>
  <li> Pip install landingai </li>
  <li> Pip install request </li>
  <li> Pip install pandas </li>
  <li> Pip install openpyxl </li>
  <li> Pip install streamlit </li>
</ol>

<h2>Smoke Tests</h2>
<p>This folder contains the execution of various APIs, including tests for creating projects of each type, uploading images, training, monitoring, creating endpoints for deployment, and making predictions.</p>
<h3>How do I run this test?</h3>
<p>You will open a terminal by pressing 'Control + Shift + Ñ' on your keyboard. Then, navigate to the Smoke-tests folder by typing 'cd Smoke-tests'.
Once you're in the Smoke-tests folder, open the file named orquestador, which is located in the Smoke-tests folder.
  [view see how the file is executed](https://drive.google.com/file/d/1ksYakD_OLG_Wi1Peq3ipn762S1S9rMxd/view?usp=sharing)
</p>
<h3>Parameters you need to change in the orchestrator:</h3>
<p>The API Key, the base URL (depending on whether you want to run this script in dev or prod), the project type, and the project name. [In this image, I've highlighted where you need to make these changes](https://drive.google.com/file/d/1V1I_Q23cCT6lUbwiWsTsgoR1PWV1HUun/view?usp=sharing).</p>
<h2>Large Images</h2>
<p>In this folder, you'll find training with advanced options, the training monitor, and the get metrics.
<h3>How do I run this test?</h3>
<p>You will open a terminal by pressing Control + Shift + Ñ on your keyboard. Then, navigate to the Large images folder by typing cd Large images.
Once you're in the Large images folder, open the file named orquestador, which is located in the Large images folder, and execute it in the same way as the smoke tests, by clicking on the run icon.</p>
<h3>Parameters you need to change in the orchestrator:</h3>
<p>The only parameter that needs to be changed is where the Excel file will be exported, which is in the reports folder located in the apis folder.</p>

