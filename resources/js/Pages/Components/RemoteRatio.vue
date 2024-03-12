<template>
    <div class="bg-white shadow-md border border-gray-200 py-4 px-4 rounded-lg">
        <h3 class="pb-3">Remote Ratio</h3>
        <PieChart :chartData="chartData" :options="options"  />
    </div>
</template>

<script>
import { defineComponent, onMounted, ref } from 'vue';
import { PieChart } from 'vue-chart-3';
import { Chart, registerables } from "chart.js";
import axios from 'axios';

Chart.register(...registerables);

export default defineComponent({
    name: 'RemoteRatio',
    components: { PieChart },
    setup() {

        const chartData = ref({});

        const fetchData = async () => {
            try {
                const response = await axios.get('https://4wasju0f2f.execute-api.us-east-1.amazonaws.com/dev/salaries/remote-ratio');
                const data = JSON.parse(response.data.data);
                const labels = data.map(item => item.remote_type);
                const values = data.map(item => item.remote_count);

                chartData.value = {
                    labels: labels,
                    datasets: [
                        {
                            data: values,
                            backgroundColor: ['#77CEFF', '#0079AF', '#123E6B']
                        },
                    ],
                }

            } catch (error) {
                console.log(error);
            }
        }

        onMounted(() => {
            fetchData();
        });

        const options = {
            plugins: {
                legend: {
                    display: true
                }
            }
        }

        return { chartData, options };
    },
});
</script>
