<?php

namespace App\Http\Controllers;

use App\Models\Cliente;
use Illuminate\Http\Request;

class ClienteController extends Controller
{
    public function index()
    {
        $clientes = Cliente::with('pedidos')->get();
        return response()->json($clientes);
    }

    public function store(Request $request)
    {

        $request->validate([
            'nombre' => 'required',
            'apellido' => 'required',
            'email' => 'required|email|unique:clientes',
            'telefono' => 'required'
        ], [
            'nombre.required' => 'El nombre es requerido',
            'apellido.required' => 'El apellido es requerido',
            'email.required' => 'El email es requerido',
            'email.email' => 'El email no es válido',
            'email.unique' => 'El email ya está en uso',
            'telefono.required' => 'El teléfono es requerido'
        ]);

        $cliente = Cliente::create($request->all());
        return response()->json($cliente,201);
    }

    public function show($id)
    {
        $cliente = Cliente::with('pedidos')->find($id);
        return response()->json($cliente);
    }

    public function update(Request $request, $id)
    {
        $request->validate([
            'email' => 'nullable|email|unique:clientes,email,' . $id,
        ], [
            'email.email' => 'El email no es válido',
            'email.unique' => 'El email ya está en uso'
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
