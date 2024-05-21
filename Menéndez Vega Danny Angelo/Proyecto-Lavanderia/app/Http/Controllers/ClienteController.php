<?php

namespace App\Http\Controllers;

use App\Models\Cliente;
use Illuminate\Http\Request;

class ClienteController extends Controller
{
    public function index()
    {
        $clientes = Cliente::all();
        return response()->json($clientes);
    }

    public function store(Request $request)
    {
        $request->validate([
            'nombre' => 'required',
            'apellido' => 'required',
            'email' => 'required|email|unique:clientes',
            'telefono' => 'required'
        ]);

        $cliente = Cliente::create($request->all());
        return response()->json($cliente);
    }

    public function show($id)
    {
        $cliente = Cliente::find($id);
        return response()->json($cliente);
    }

    public function update(Request $request, $id)
    {
        $request->validate([
            'email' => 'nullable|email|unique:clientes,email,' . $id,
        ]);
        $cliente = Cliente::find($id);
        $cliente->update($request->all());
        return response()->json($cliente);
    }

    public function destroy($id)
    {
        $cliente = Cliente::find($id);
        $cliente->update(['activo' => false]);
        return response()->json(null, 204);
    }
}
