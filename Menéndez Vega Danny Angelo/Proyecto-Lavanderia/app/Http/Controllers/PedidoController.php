<?php

namespace App\Http\Controllers;

use App\Models\Pedido;
use Illuminate\Http\Request;

class PedidoController extends Controller
{

    public function index()
    {
        $pedidos = Pedido::all();
        return response()->json($pedidos);
    }

    public function store(Request $request)
    {
        $request->validate([
            'id_cliente' => 'required|exists:clientes,id_cliente',
            'id_metodo_pago' => 'required|exists:metodo_pago,id_metodo_pago',
            'cantidad_pedido' => 'required|numeric',
        ]);

        $pedido = Pedido::create($request->all());
        return response()->json($pedido);
    }

    public function show($id)
    {
        $pedido = Pedido::find($id);
        return response()->json($pedido);
    }

    public function update(Request $request, $id)
    {
        $request->validate([
            'id_cliente' => 'required|exists:clientes,id_cliente',
            'id_metodo_pago' => 'required|exists:metodo_pago,id_metodo_pago',
            'cantidad_pedido' => 'required|numeric',
        ]);

        $pedido = Pedido::find($id);
        $pedido->update($request->all());
        return response()->json($pedido);
    }

    public function destroy($id)
    {
        $pedido = Pedido::find($id);
        $pedido->update(['estado' => false]);
        return response()->json(['message' => 'Pedido ']);
    }
}
