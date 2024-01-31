<template>
    <div class="bg-white shadow-md border border-gray-200 py-4 px-4 rounded-lg">
        <h3 class="pb-3">Salario / Posición</h3>
    <DoughnutChart :chartData="testData" />
    </div>
  </template>

  <script lang="ts">
  import { defineComponent } from 'vue';
  import { DoughnutChart } from 'vue-chart-3';
  import { Chart, registerables } from "chart.js";

  Chart.register(...registerables);

  export default defineComponent({
    name: 'PositionSalary',
    components: { DoughnutChart },
    setup() {
      const testData = {
        labels: ['Paris', 'Nîmes', 'Toulon', 'Perpignan', 'Autre'],
        datasets: [
          {
            data: [30, 40, 60, 70, 5],
            backgroundColor: ['#77CEFF', '#0079AF', '#123E6B', '#97B0C4', '#A5C8ED'],
          },
        ],
      };

      return { testData };
    },
  });
  </script>
