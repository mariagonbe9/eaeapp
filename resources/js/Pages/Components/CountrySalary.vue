<template>
    <div class="bg-white shadow-md border border-gray-200 py-4 px-4 rounded-lg">
        <h3 class="pb-3">Salarios / País</h3>
        <BarChart :chartData="chartData" :options="options"  />
    </div>
</template>

<script>
import { defineComponent, onMounted, ref } from 'vue';
import { BarChart } from 'vue-chart-3';
import { Chart, registerables } from "chart.js";
import axios from 'axios';

Chart.register(...registerables);

export default defineComponent({
    name: 'CountrySalary',
    components: { BarChart },
    setup() {

        const chartData = ref({});

        const numberToColor = function(number, min, max) {
            let normalized = (number - min) / (max - min);
            let hue = (250 + normalized * (-60)).toFixed(1);
            return `hsl(${hue}, 70%, 50%)`;
        }

        const fetchData = async () => {
            try {
                const response = await axios.get('');
                const data = JSON.parse(response.data.data);
                const labels = data.map(item => item.employee_residence);
                const values = data.map(item => item.average_salary);
                const min = Math.min(...values);
                const max = Math.max(...values);
                const colors = values.map(item => numberToColor(item, min, max));

                chartData.value = {
                    labels: labels,
                    datasets: [
                        {
                            data: values,
                            backgroundColor: colors,
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
                    display: false
                }
            }
        }

        return { chartData, options };
    },
});
</script>
