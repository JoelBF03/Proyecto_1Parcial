<?php

use App\Http\Controllers\AuthController;
use App\Http\Controllers\ClienteController;
use App\Http\Controllers\PedidoController;
use App\Http\Controllers\TipoServicioController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;


Route::post('login',[AuthController::class, 'login'])->middleware('guest:sanctum');

Route::middleware('auth:sanctum')->group(function () {

    Route::resource('cliente', ClienteController::class);
    Route::resource('pedido', PedidoController::class);
    Route::resource('tipo_servicio', TipoServicioController::class);
    Route::post('logout', [AuthController::class, 'logout']);

});
