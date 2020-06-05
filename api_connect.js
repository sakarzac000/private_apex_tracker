async function queryApis(platformInput, nameInput) {
    const fetch = require("node-fetch");

    const postsPromise = fetch('https://apex-legends-tracker-api.herokuapp.com/', {
        method: 'GET',
        headers: {
            platform: platformInput,
            name: nameInput
        }
    });

    const posts = await postsPromise.then(res => res.json());
    console.log(posts);
}

console.log(queryApis('origin', 'zylbrad'))