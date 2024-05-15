<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('pedido_servicio', function (Blueprint $table) {
            $table->id();
            $table->foreignId('id_pedido')->references('id_pedido')->on('pedidos');
            $table->foreignId('id_tipo_servicio')->references('id_tipo_servicio')->on('tipo_servicio');
            $table->decimal('total_servicio', 8, 2);
            $table->string('descripcion');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('pedido_servicio');
    }
};
