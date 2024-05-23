<?php

use App\Http\Controllers\AuthController;
use App\Http\Controllers\ClienteController;
use App\Http\Controllers\MetodoPagoController;
use App\Http\Controllers\PedidoController;
use App\Http\Controllers\TipoServicioController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::post('login',[AuthController::class, 'login'])->middleware('guest:sanctum');

Route::middleware('auth:sanctum')->group(function () {

    Route::resource('cliente', ClienteController::class);
    Route::resource('pedido', PedidoController::class);
    Route::resource('tipo_servicio', TipoServicioController::class);
    Route::resource('metodo_pago', MetodoPagoController::class);
    Route::post('logout', [AuthController::class, 'logout']);

});

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});
