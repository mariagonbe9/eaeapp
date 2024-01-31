<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration {
    public function up(): void
    {
        Schema::create('salaries', function (Blueprint $table) {
            $table->id();
            $table->integer('work_year')->nullable();
            $table->string('experience_level')->nullable();
            $table->string('employment_type')->nullable();
            $table->string('job_title')->nullable();
            $table->integer('salary')->nullable();
            $table->string('salary_currency')->nullable();
            $table->integer('salary_in_usd')->nullable();
            $table->string('employee_residence')->nullable();
            $table->integer('remote_ratio')->nullable();
            $table->string('company_location')->nullable();
            $table->string('company_size')->nullable();
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('salaries');
    }
};
