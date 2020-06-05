async function queryApis(platformInput, nameInput) {



    const postsPromise = fetch('https://apex-legends-tracker-api.herokuapp.com/', {
        method: 'GET',
        mode: 'no-cors',
        headers: {
            platform: platformInput,
            name: nameInput,
        }
    });

    const posts = await postsPromise.then(res =>{
        console.log(res)
    }); 

    return posts;
}