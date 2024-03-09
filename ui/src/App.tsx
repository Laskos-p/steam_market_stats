import { Outlet, RouterProvider, createBrowserRouter } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Loader from "./components/Loader";
import { Suspense, lazy } from "react";

const Items = lazy(() => import("./pages/Items"));
const Item = lazy(() => import("./pages/Item"));

const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <Home />,
        index: true,
      },
      {
        path: "items",
        element: <Items />,
      },
      {
        path: "items/:id",
        element: <Item />,
      },
    ],
  },
]);

export default function App() {
  return <RouterProvider router={router} fallbackElement={<Loader />} />;
}

function Layout() {
  return (
    <div className="container mx-auto grid min-h-screen grid-rows-[auto_1fr] gap-4 p-4 ">
      <header className="sticky top-4">
        <Navbar />
      </header>
      <main>
        <Suspense fallback={<Loader className="mx-auto" />}>
          <Outlet />
        </Suspense>
      </main>
    </div>
  );
}
