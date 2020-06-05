function queryApis(platformInput, nameInput) {


    console.log('test a')
    const postsPromise = fetch('https://apex-legends-tracker-api.herokuapp.com/', {
        method: 'GET',
        headers: {
            platform: platformInput,
            name: nameInput,
        }
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log("Error querying API: ", error))
}

queryApis('origin', 'tvc_hazed');