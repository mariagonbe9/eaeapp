<template>
    <div class="grid grid-cols-2 gap-6 ">
        <CountrySalary />
        <PositionSalary />
        <RemoteRatio />
        <YearSalary />
    </div>
</template>

<script setup>
import CountrySalary from './CountrySalary.vue';
import PositionSalary from './PositionSalary.vue';
import RemoteRatio from './RemoteRatio.vue';
import YearSalary from './YearSalary.vue';

</script>