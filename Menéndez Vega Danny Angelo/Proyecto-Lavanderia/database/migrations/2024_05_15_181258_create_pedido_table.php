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
        Schema::create('pedidos', function (Blueprint $table) {
            $table->id('id_pedido');
            $table->foreignId('id_cliente')->references('id_cliente')->on('clientes');
            $table->foreignId('id_metodo_pago')->references('id_metodo_pago')->on('metodo_pago');
            $table->integer('cantidad_pedido');
            $table->string('observacion');
            $table->date('fecha_pedido');
            $table->boolean('estado')->default(1);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('pedido');
    }
};
