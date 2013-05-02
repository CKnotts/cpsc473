db.topics.insert(
    {
        forum: 'redis',
        title: 'Does anyone know how to start Redis?',
        posts: [
            {
                user: 'bob', 
                text: "I'm trying to connect to Redis, but it doesn't seem to be running.",
                date: new Date()
            },
            {
                user: 'alice', 
                text: "Try 'sudo service start redis-server'.",
                date: new Date()
            }
        ]
    }
);

db.topics.insert(
    {
        forum: 'redis',
        title: 'Has anyone heard of Edis?',
        posts: [
            {
                user: 'carol', 
                text: "Apparently it's like Redis, but for data sets that don't fit in memory:\n\nhttp://inaka.github.io/edis/",
                date: new Date()
            }
        ]
    }
);

db.topics.insert(
    {
        forum: 'mongodb',
        title: 'Does anyone know how to start MongoDB?',
        posts: [
            {
                user: 'bob', 
                text: "I'm trying to connect to MongoDB, but it doesn't seem to be running.",
                date: new Date()
            },
            {
                user: 'alice', 
                text: "Ummm... 'sudo service start mongodb'?",
                date: new Date()
            },
            {
                user: 'carol', 
                text: "@Bob: Derp.",
                date: new Date()
            }
        ]
    }
);

