let servurl = import.meta.env.VITE_API_ENDPOINT

export async function getAllPersons() {
    const url = servurl + "/persons"
    let fetchResult = await fetch(url).catch((_) => new Response());
    try {
        let data = await fetchResult.json();
        return data;
    }
    catch {
        return []
    }
}


export async function addNewPerson(person: {last_name: string, phone_number: string}) {
    const url = servurl + "/person"
    let fetchResult = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(person)
    }).catch((_) => new Response());
    try {
        let data = await fetchResult.json();
        return data;
    }
    catch {
        return []
    }
}