<script setup>
import AppLayout from '@/Layouts/AppLayout.vue';
import FileUpload from "@/Pages/Components/FileUpload.vue";
import SalaryDashboard from "@/Pages/Components/SalaryDashboard.vue";
import {DocumentPlusIcon, FunnelIcon} from "@heroicons/vue/24/outline/index.js";
import {ref} from "vue";

defineProps({
    salaries: Object,
});

const openFileUpload = ref(false)
const handleToggleFileUpload = () => {
    openFileUpload.value = !openFileUpload.value
}
</script>

<template>
    <AppLayout title="Dashboard">
        <template #header>
            <h2 class="font-semibold text-xl text-gray-800 dark:text-gray-200 leading-tight">
                Dashboard
                <div class="float-right flex items-center">
                    <span v-if="salaries.length > 0" class="inline-flex items-center rounded-full bg-green-50 px-2 py-1 text-xs font-medium text-green-700 ring-1 ring-inset ring-green-600/20">
                        {{ salaries.length }}
                    </span>
                    <button type="button"
                            @click="handleToggleFileUpload"
                            class="ml-2 rounded-full bg-white p-1 text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
                        <span class="sr-only">Upload a file</span>
                        <DocumentPlusIcon class="h-6 w-6" aria-hidden="true"/>
                    </button>
                </div>

            </h2>
        </template>

        <div class="py-12">
            <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
                <div class="bg-transparent dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg">
                    <SalaryDashboard/>
                    <FileUpload :open="openFileUpload" @toggle-file-upload="handleToggleFileUpload"/>
                </div>
            </div>
        </div>
    </AppLayout>
</template>
