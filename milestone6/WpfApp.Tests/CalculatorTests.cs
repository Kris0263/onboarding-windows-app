using NUnit.Framework;
using WpfApp.ViewModels;

namespace WpfApp.Tests
{
    public class CalculatorTests
    {
        private CalculatorViewModel _viewModel;

        [SetUp]
        public void Setup()
        {
            _viewModel = new CalculatorViewModel();
        }

        [Test]
        public void Square_PositiveNumber_ReturnsCorrectResult()
        {
            var result = _viewModel.Square(4);
            NUnit.Framework.Assert.AreEqual(16, result);

        }

        [Test]
        public void Square_NegativeNumber_ReturnsPositiveResult()
        {
            var result = _viewModel.Square(-3);
            NUnit.Framework.Assert.AreEqual(9, result);
        }

        [Test]
        public void Square_Zero_ReturnsZero()
        {
            var result = _viewModel.Square(0);
            NUnit.Framework.Assert.AreEqual(0, result);
        }
    }
}
