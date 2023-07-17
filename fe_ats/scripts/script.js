fetch('http://localhost:5000/api/getSumIncome')
  .then(response => response.json())
  .then(data => {
    // Process the retrieved data
    console.log(data);

    const PersonalData_name = document.getElementById('personalData_name');
    const PersonalData_jobApplication = document.getElementById('personalData_jobApplication');
    const PersonalData_summary = document.getElementById('personalData_summary');
    const PersonalData_address = document.getElementById('personalData_address');
    const PersonalData_email = document.getElementById('personalData_email');
    
    // Check if data.message exists
    if (data) {
      PersonalData_name.textContent = data.name;
      PersonalData_jobApplication.textContent = data.job_application;
      PersonalData_email.textContent = data.email;
      PersonalData_summary.textContent = data.summary;
      PersonalData_address.textContent = data.address;
    } else {
      console.log('No data found.');
    }
  })
  // .catch(error => {
  //   // Handle any errors that occurred
  //   console.error('Error:', error);
  // });
