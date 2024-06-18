<script lang="ts">
import { getAllPersons } from '../database/person';

export default {
    name: "ListPersons",
    data() {
        return {
            personList: []
        }
    },
    methods: {
        async getPersons() {
            let data = await getAllPersons()
            this.personList = data
        }
    },
    mounted() {
        this.getPersons();
    }
}
</script>

<template>
    <h1>List all persons</h1>
    <button @click="this.getPersons">Reload</button>
    <router-link :to="{ name: 'home'}">
        <button>Return to homepage</button>
    </router-link>
    <section>
        <table id="tablePerson" class="table mb-0">
            <thead>
                <tr>
                    <th>Last name</th>
                    <th>Phone number</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="person in this.personList" :key="person.id">
                    <td>{{ person[0] }}</td>
                    <td>{{ person[1] }}</td>
                </tr>
            </tbody>
        </table>
    </section>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}

section {
    align-content: center;
    padding: 5%;
}

thead {
    background-color: #218ffe;
    color: white;
}

th {
    text-align: center;
}

tr {
    height: fit-content;
    width: fit-content;
}

td {
    background-color: #3e3e3e;
    margin-left: 2%;
    margin-right: 2%;
}
</style>
